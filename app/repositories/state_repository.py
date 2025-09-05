from typing import Optional, List,Iterator
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from app.db.models.state import State
from app.schemas.state import StateCreate, StateUpdate

class StateRepository:


    def get_all(self, db: Session, page: int = 1, items_per_page: int = 10, q: Optional[str] = None) -> List[State]:
        stmt = select(State).order_by(State.id)
        if q:
            stmt = stmt.where(State.name.ilike(f"%{q}%"))
        stmt = stmt.offset((page - 1) * items_per_page).limit(items_per_page)
        return db.execute(stmt).scalars().all()

    def iter_all(self, db: Session, q: Optional[str] = None, chunk_size: int = 1000) -> Iterator[State]:
        stmt = select(State).order_by(State.id)
        if q:
            stmt = stmt.where(State.name.ilike(f"%{q}%"))
        stmt = stmt.execution_options(stream_results=True, yield_per=chunk_size)
        for row in db.execute(stmt).scalars():
            yield row

    @staticmethod
    def count(db: Session, q: Optional[str] = None) -> int:
        stmt = select(func.count()).select_from(State)
        if q:
            stmt = stmt.where(State.name.ilike(f"%{q}%"))
        return db.execute(stmt).scalar_one()
    """ def get_all(self,db:Session):
        return db.query(State).all() """
    
    def get_by_id(self, db: Session, state_id: int):
        return db.query(State).filter(State.id == state_id).first()
    
    def create(self,db:Session, state:StateCreate):
        db_state = State(**state.dict())
        db.add(db_state)
        db.commit()
        db.refresh(db_state)
        return db_state
    