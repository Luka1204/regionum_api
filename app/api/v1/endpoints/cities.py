from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.city import CityCreate, CityUpdate, CityRead
from app.services.city_service import CityService
from typing import Optional
from app.repositories.city_repository import CityRepository

router = APIRouter()
repo = CityRepository()
service = CityService(repo)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/p={page}", response_model=list[CityRead])
def list_cities(page:Optional[int], db:Session = Depends(get_db)):
    """
    List all cities
    """
    if page == None:
        page = 1
    cities = service.list_cities(db,page)
    return cities

@router.get("/{city_id}", response_model=CityRead)
def get_city(city_id:int, db:Session = Depends(get_db)):
    """
    Get a city by ID
    """
    city = service.get_city(db, city_id)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@router.post("/", response_model=CityRead)
def create_city(city: CityCreate, db: Session = Depends(get_db)):
    """
    Create a new city
    """
    return service.create_city(db, city)
