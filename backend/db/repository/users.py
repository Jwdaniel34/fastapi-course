from sqlalchemy.orm import Session

#schemas for fastapi pydantic
from schemas.users import UserCreate
#models from sqlalchemy database
from db.models.users import User
#hashing from core to protect the password
from core.hashing import Hasher


def create_new_user(user: UserCreate, db: Session):
    user = User(username= user.username, # Column(user)
                email = user.email,  #Column(email)
                hashed_password=Hasher.get_password_hash(user.password), #Column(password)
                is_active=True, # Column(is_active) allow user to login
                is_superuser=False # Column(is_active) False to not allow users to change website
                )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user