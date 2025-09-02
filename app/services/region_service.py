from sqlalchemy.orm import Session
from app.repositories.region_repository import RegionRepository
from app.schemas.region import RegionCreate, RegionUpdate

class RegionService:
    def __init__(self,repo:RegionRepository):
        self.repo = repo
    def list_regions(self, db: Session):
        return self.repo.get_all(db)
    def get_region(self, db: Session, region_id: int):
        return self.repo.get_by_id(db, region_id)
    def create_region(self, db: Session, region: RegionCreate):
        return self.repo.create(db, region)