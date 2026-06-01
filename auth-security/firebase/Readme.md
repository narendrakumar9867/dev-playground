# Firebase Auth Flow

This folder contains a small FastAPI app that uses Firebase Admin SDK for signup and token verification.

## What This Implementation Does

- Creates a Firebase user with email and password.
- Stores a small user profile in Firestore when Firestore is available.
- Verifies Firebase ID tokens on protected requests.
- Keeps the signup flow backend-based using the service account JSON.

## Current API Flow

### 1. Signup

Endpoint: `POST /signup`

Request body:

```json
{
	"email": "testuser@example.com",
	"password": "Test@12345",
	"display_name": "Test User"
}
```

What happens:

- `firebase_admin.auth.create_user()` creates the auth user.
- The user profile is saved in Firestore under `users/{uid}`.
- If Firestore is disabled, signup still succeeds because profile save is best effort.

Example response:

```json
{
	"message": "Successfully created user abc123",
	"uid": "abc123"
}
```

### 2. Ping / Protected Check

Endpoint: `POST /ping`

This endpoint requires a Firebase ID token in the `Authorization` header.

Header:

```http
Authorization: Bearer <FIREBASE_ID_TOKEN>
```

Example response:

```json
{
	"uid": "abc123",
	"email": "testuser@example.com"
}
```

## How Frontend Connects

The frontend should use Firebase Authentication SDK to sign in the user and get an ID token. Then send that token to the backend.

### Frontend Sign In Flow

1. User signs in on the frontend using Firebase Auth.
2. Firebase returns a logged-in user object.
3. Frontend calls `getIdToken()` on that user.
4. Frontend sends the token to FastAPI in the `Authorization` header.

### Example Frontend Code

```javascript
import { getAuth, signInWithEmailAndPassword } from "firebase/auth";

const auth = getAuth();

async function loginAndCallPing(email, password) {
	const credential = await signInWithEmailAndPassword(auth, email, password);
	const idToken = await credential.user.getIdToken();

	const response = await fetch("http://127.0.0.1:8000/ping", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			Authorization: `Bearer ${idToken}`,
		},
	});

	return await response.json();
}
```

## Postman Testing

### Signup

- Method: `POST`
- URL: `http://127.0.0.1:8000/signup`
- Body type: `raw` + `JSON`

```json
{
	"email": "testuser@example.com",
	"password": "Test@12345",
	"display_name": "Test User"
}
```

### Ping

- Method: `POST`
- URL: `http://127.0.0.1:8000/ping`
- Header: `Authorization: Bearer <idToken>`

## Running Locally

From this folder on Windows:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

## Required Files

- `serviceAccountKey.json` must exist in this folder for Firebase Admin SDK.

## Important Notes

- `password` must be at least 6 characters.
- Firestore save is optional for signup right now.
- The backend does not currently handle frontend password login itself.
- If you want backend login too, you need a separate login flow or Firebase client sign-in on the frontend.

## API Summary

- `GET /` - health message
- `POST /signup` - create Firebase user
- `POST /ping` - verify Firebase ID token

