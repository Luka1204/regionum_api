from fastapi import APIRouter

from app.api.v1.endpoints import countries

api_router = APIRouter()
api_router.include_router(countries.router, prefix="/countries", tags=["countries"])