from sqlalchemy.orm import Session
from app.repositories.country_repository import CountryRepository
from app.schemas.country import CountryCreate, CountryUpdate

class CountryService:
    def __init__(self,repo:CountryRepository):
        self.repo = repo
    def list_countries(self, db: Session):
        return self.repo.get_all(db)
    def get_country(self, db: Session, country_id: int):
        return self.repo.get_by_id(db, country_id)
    def create_country(self, db: Session, country: CountryCreate):
        return self.repo.create(db, country)