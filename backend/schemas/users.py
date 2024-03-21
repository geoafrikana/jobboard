from typing import Optional
from pydantic import BaseModel, EmailStr

class USerCreate(BaseModel):
    username: str
    email : EmailStr
    password: str