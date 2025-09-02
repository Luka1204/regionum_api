from sqlalchemy.orm import Session
from app.db.models.region import Region
from app.schemas.region import RegionCreate, RegionUpdate

class RegionRepository:
    def get_all(self,db:Session):
        return db.query(Region).all()
    
    def get_by_id(self, db: Session, region_id: int):
        return db.query(Region).filter(Region.id == region_id).first()
    
    def create(self,db:Session, region:RegionCreate):
        db_region = Region(**region.dict())
        db.add(db_region)
        db.commit()
        db.refresh(db_region)
        return db_region
    