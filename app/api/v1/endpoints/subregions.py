from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.subregion import SubRegionCreate, SubRegionUpdate, SubRegionRead
from app.services.subregion_service import SubRegionService
from app.repositories.subregion_repository import SubRegionRepository

router = APIRouter()
repo = SubRegionRepository()
service = SubRegionService(repo)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[SubRegionRead])
def list_subregions(db:Session = Depends(get_db)):
    """
    List all subregion
    """
    subregions = service.list_subregions(db)
    return subregions

@router.get("/{subregion_id}", response_model=SubRegionRead)
def list_subregion(subregion_id:int, db:Session = Depends(get_db)):
    """
    Get a subregion by ID
    """
    subregion = service.get_subregion(db, subregion_id)
    if not subregion:
        raise HTTPException(status_code=404, detail="Sub-Region not found")
    return subregion

@router.post("/", response_model=SubRegionRead)
def create_subregion(region: SubRegionCreate, db: Session = Depends(get_db)):
    """
    Create a new subregion
    """
    return service.create_subregion(db, region)
