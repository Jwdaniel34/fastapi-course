from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


# General base model to inherit from when creating CRUD models, working as a data validator
class JobBase(BaseModel):
    title : Optional[str] = None
    company : Optional[str] = None
    company_url : Optional[str] = None
    location : Optional[str] = "Remote"
    description : Optional[str] = None
    date_post: Optional[date] = datetime.now().date()


# Inheriting from JobBase using thier properties
class JobCreate(JobBase):
    title : str
    company : str
    location : str
    description : str

# show response model using show
class ShowJob(JobBase):
    title : str
    company : str
    company_url : Optional[str]
    location : str
    description : Optional[str]
    date_post : date

    class Config():
        orm_mode = True