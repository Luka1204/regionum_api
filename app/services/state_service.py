from sqlalchemy.orm import Session
from app.repositories.state_repository import StateRepository
from app.schemas.state import StateCreate, StateUpdate

class StateService:
    def __init__(self,repo:StateRepository):
        self.repo = repo
    def list_states(self, db: Session):
        return self.repo.get_all(db)
    def get_state(self, db: Session, state_id: int):
        return self.repo.get_by_id(db, state_id)
    def create_state(self, db: Session, state: StateCreate):
        return self.repo.create(db, state)