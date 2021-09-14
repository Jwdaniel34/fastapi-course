from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    usesrname : str
    email : EmailStr
    password : str


