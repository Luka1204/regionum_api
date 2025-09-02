from sqlalchemy.orm import Session
from app.db.models.state import State
from app.schemas.state import StateCreate, StateUpdate

class StateRepository:
    def get_all(self,db:Session):
        return db.query(State).all()
    
    def get_by_id(self, db: Session, state_id: int):
        return db.query(State).filter(State.id == state_id).first()
    
    def create(self,db:Session, state:StateCreate):
        db_state = State(**state.dict())
        db.add(db_state)
        db.commit()
        db.refresh(db_state)
        return db_state
    