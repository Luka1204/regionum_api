from sqlalchemy.orm import Session
from app.db.models.subregion import SubRegion
from app.schemas.subregion import SubRegionCreate, SubRegionUpdate

class SubRegionRepository:
    def get_all(self,db:Session):
        return db.query(SubRegion).all()
    
    def get_by_id(self, db: Session, subregion_id: int):
        return db.query(SubRegion).filter(SubRegion.id == subregion_id).first()
    
    def create(self,db:Session, subregion:SubRegionCreate):
        db_subregion = SubRegion(**subregion.dict())
        db.add(db_subregion)
        db.commit()
        db.refresh(db_subregion)
        return db_subregion
