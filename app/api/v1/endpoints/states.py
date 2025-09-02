from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.state import StateCreate, StateUpdate, StateRead
from app.services.state_service import StateService
from app.repositories.state_repository import StateRepository

router = APIRouter()
repo = StateRepository()
service = StateService(repo)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[StateRead])
def list_states(db:Session = Depends(get_db)):
    """
    List all states
    """
    regions = service.list_states(db)
    return regions

@router.get("/{state_id}", response_model=StateRead)
def list_state(state_id:int, db:Session = Depends(get_db)):
    """
    Get a state by ID
    """
    state = service.get_state(db, state_id)
    if not state:
        raise HTTPException(status_code=404, detail="State not found")
    return state

@router.post("/", response_model=StateRead)
def create_state(region: StateCreate, db: Session = Depends(get_db)):
    """
    Create a new state
    """
    return service.create_state(db, region)
