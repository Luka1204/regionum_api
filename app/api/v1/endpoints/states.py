from fastapi import APIRouter, Depends,HTTPException
from fastapi.responses import StreamingResponse
import orjson 
from sqlalchemy.orm import Session
from app.db.session import SessionLocal

from sqlalchemy import select, func
from typing import Optional

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


""" 

    List all states
    
 """

@router.get("/p/{page}", response_model=list[StateRead])
def list_states(page: int, db: Session = Depends(get_db), page_size: int = 10, q: Optional[str] = None):
    total = repo.count(db, q)

    # Caso sin datos
    if total == 0:
        return []

    out_of_range = (page <= 0) or ((page - 1) * page_size >= total)

    if out_of_range:
        # → devolver TODO en streaming (sin caché)
        def json_array_stream():
            first = True
            yield b"["
            for item in service.iter_all_states(db, q=q, chunk_size=1000):
                if not first:
                    yield b","
                first = False
                yield orjson.dumps(item)
            yield b"]"
        return StreamingResponse(json_array_stream(), media_type="application/json")

    # Página válida → usa caché
    items = service.list_states(db, page=page, page_size=page_size, q=q)
    return items

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
