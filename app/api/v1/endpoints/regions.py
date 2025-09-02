from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.region import RegionCreate, RegionUpdate, RegionRead
from app.services.region_service import RegionService
from app.repositories.region_repository import RegionRepository

router = APIRouter()
repo = RegionRepository()
service = RegionService(repo)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[RegionRead])
def list_regions(db:Session = Depends(get_db)):
    """
    List all regions
    """
    regions = service.list_regions(db)
    return regions

@router.get("/{region_id}", response_model=RegionRead)
def list_region(region_id:int, db:Session = Depends(get_db)):
    """
    Get a region by ID
    """
    region = service.get_region(db, region_id)
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")
    return region

@router.post("/", response_model=RegionRead)
def create_region(region: RegionCreate, db: Session = Depends(get_db)):
    """
    Create a new region
    """
    return service.create_region(db, region)
