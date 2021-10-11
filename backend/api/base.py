from fastapi import APIRouter

from api.v1 import route_users
from api.v1 import route_jobs
from api.v1 import route_login

api_router = APIRouter()

api_router.include_router(route_users.router, prefix="/user", tags=["User"])
api_router.include_router(route_jobs.router, prefix="/job", tags=["Job"])
api_router.include_router(route_login.router,prefix="/login", tags=["Login"])