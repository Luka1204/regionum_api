from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.country import CountryCreate, CountryUpdate,CountryRead
from app.services.country_service import CountryService
from app.repositories.country_repository import CountryRepository

router = APIRouter()
repo = CountryRepository()
service = CountryService(repo)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[CountryRead])
def list_countries(db:Session = Depends(get_db)):
    """
    List all countries
    """
    countries = service.list_countries(db)
    return countries

@router.get("/{country_id}", response_model=CountryRead)
def get_country(country_id:int, db:Session = Depends(get_db)):
    """
    Get a country by ID
    """
    country = service.get_country(db, country_id)
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    return country

@router.post("/", response_model=CountryRead)
def create_country(country: CountryCreate, db: Session = Depends(get_db)):
    """
    Create a new country
    """
    return service.create_country(db, country)
