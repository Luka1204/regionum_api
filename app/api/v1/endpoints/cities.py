from fastapi import APIRouter, Depends,HTTPException
from fastapi.responses import StreamingResponse
import orjson 
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.city import CityRead,CityCreate,CityUpdate
from app.repositories.city_repository import CityRepository
from app.services.city_service import CityService
from sqlalchemy import select, func
from typing import Optional

router = APIRouter()
service = CityService(CityRepository())

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/p/{page}", response_model=list[CityRead])
def list_cities(page: int, db: Session = Depends(get_db), page_size: int = 10, q: Optional[str] = None):
    total = CityRepository.count(db, q)

    # Caso sin datos
    if total == 0:
        return []

    out_of_range = (page <= 0) or ((page - 1) * page_size >= total)

    if out_of_range:
        # → devolver TODO en streaming (sin caché)
        def json_array_stream():
            first = True
            yield b"["
            for item in service.iter_all_cities(db, q=q, chunk_size=1000):
                if not first:
                    yield b","
                first = False
                yield orjson.dumps(item)
            yield b"]"
        return StreamingResponse(json_array_stream(), media_type="application/json")

    # Página válida → usa caché
    items = service.list_cities(db, page=page, page_size=page_size, q=q)
    return items

@router.get("/{city_id}", response_model=CityRead)
def get_city(city_id:int, db:Session = Depends(get_db)):
    """
    Get a city by ID
    """
    city = service.get_city(db, city_id)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@router.get("/cityByName/{city_name}",response_model=list[CityRead])
def get_city_by_name(city_name:str, db:Session=Depends(get_db)):
    city = service.get_city_by_name(db,city_name)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@router.get("/cityByStateCode/{state_code}",response_model=list[CityRead])
def get_city_by_state_code(state_code:str, db:Session=Depends(get_db)):
    city = service.get_city_by_state_code(db,state_code)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@router.get("/cityByStateId/{state_id}",response_model=list[CityRead])
def get_city_by_state_code(state_id:int, db:Session=Depends(get_db)):
    city = service.get_city_by_state_id(db,state_id)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@router.get("/cityByCountryId/{country_id}",response_model=list[CityRead])
def get_city_by_country_id(country_id:int, db:Session=Depends(get_db)):
    city = service.get_city_by_country_id(db,country_id)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@router.get("/cityByCountryCode/{country_code}",response_model=list[CityRead])
def get_city_by_country_code(country_code:str, db:Session=Depends(get_db)):
    city = service.get_city_by_country_code(db,country_code)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@router.post("/", response_model=CityRead)
def create_city(city: CityCreate, db: Session = Depends(get_db)):
    """
    Create a new city
    """
    return service.create_city(db, city)

