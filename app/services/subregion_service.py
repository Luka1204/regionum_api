from sqlalchemy.orm import Session
from app.repositories.subregion_repository import SubRegionRepository
from app.schemas.subregion import SubRegionCreate, SubRegionUpdate

class SubRegionService:
    def __init__(self,repo:SubRegionRepository):
        self.repo = repo
    def list_subregions(self, db: Session):
        return self.repo.get_all(db)
    def get_subregion(self, db: Session, subregion_id: int):
        return self.repo.get_by_id(db, subregion_id)
    def create_subregion(self, db: Session, subregion: SubRegionCreate):
        return self.repo.create(db, subregion)