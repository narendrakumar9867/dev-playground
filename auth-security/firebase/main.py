from fastapi import APIRouter, FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from firebase_admin import auth

from config import db
from models import User
from schema import PingResponse, SignupRequest, SignupResponse


app = FastAPI(title="Firebase Auth API")
router = APIRouter(tags=["Authentication"])


@app.get("/")
def homepage():
    return {"message": "Welcome to Firebase auth"}


allow_all = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_all,
    allow_credentials=True,
    allow_methods=allow_all,
    allow_headers=allow_all,
)


def _normalize_bearer_token(authorization: str | None) -> str:
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header is required",
        )

    if authorization.lower().startswith("bearer "):
        return authorization[7:].strip()

    return authorization.strip()


def _store_user_profile(user_record, display_name: str | None) -> None:
    user = User(
        uid=user_record.uid,
        email=user_record.email,
        display_name=display_name,
    )
    try:
        db.collection("users").document(user.uid).set(user.dict(exclude_none=True))
    except Exception:
        # Signup should still succeed if Firestore is not enabled yet.
        pass


@router.post("/signup", response_model=SignupResponse)
async def signup(payload: SignupRequest):
    try:
        user_record = auth.create_user(
            email=payload.email,
            password=payload.password,
            display_name=payload.display_name,
        )
        _store_user_profile(user_record, payload.display_name)
        return SignupResponse(
            message=f"Successfully created user {user_record.uid}",
            uid=user_record.uid
        )
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error creating user: {exc}",
        )


@router.post("/ping", response_model=PingResponse)
async def validate(request: Request):
    token = _normalize_bearer_token(request.headers.get("authorization"))
    decoded_token = auth.verify_id_token(token)
    return PingResponse(uid=decoded_token["uid"], email=decoded_token.get("email"))


app.include_router(router)

