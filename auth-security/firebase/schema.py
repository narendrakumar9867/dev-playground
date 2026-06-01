from typing import Optional
from pydantic import BaseModel, Field


class SignupRequest(BaseModel):
	email: str
	password: str = Field(min_length=6)
	display_name: Optional[str] = None


class SignupResponse(BaseModel):
	message: str
	uid: Optional[str] = None


class PingResponse(BaseModel):
	uid: str
	email: Optional[str] = None
