from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    uid: str
    email: str
    display_name: Optional[str] = None

