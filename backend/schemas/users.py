from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username : str
    email : EmailStr
    password : str


class ShowUser(BaseModel):
    username : str
    email : EmailStr
    is_active : bool

    # convert object to a dictionary
    class Config():
        orm_mode = True