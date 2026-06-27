from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine
from repository import UserRepository


Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

def get_user_repo(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)

        
@app.post("/users/", status_code=201)
def create_user(name: str, email: str, repo: UserRepository = Depends(get_user_repo)):
    return repo.create(name, email)


@app.get("/users/")
def get_users(repo: UserRepository = Depends(get_user_repo)):
    return repo.get_all()


@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, email: str, repo: UserRepository = Depends(get_user_repo)):
    user = repo.update(user_id, name, email)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, repo: UserRepository = Depends(get_user_repo)):
    deleted = repo.delete(user_id)
    
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"message" : "User deleted"}

