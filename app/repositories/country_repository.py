from sqlalchemy.orm import Session
from app.db.models.country import Country
from app.schemas.country import CountryCreate, CountryUpdate

class CountryRepository:
    def get_all(self,db:Session):
        return db.query(Country).all()
    
    def get_by_id(self, db: Session, country_id: int):
        return db.query(Country).filter(Country.id == country_id).first()
    
    def create(self,db:Session, country:CountryCreate):
        db_country = Country(**country.dict())
        db.add(db_country)
        db.commit()
        db.refresh(db_country)
        return db_country
