from sqlalchemy.orm import Session
from app.repositories.city_repository import CityRepository
from app.schemas.city import CityCreate, CityUpdate

class CityService:
    def __init__(self,repo:CityRepository):
        self.repo = repo
    def list_cities(self, db: Session,page:int):
        return self.repo.get_all(db,page)
    def get_city(self, db: Session, city_id: int):
        return self.repo.get_by_id(db, city_id)
    def create_city(self, db: Session, city: CityCreate):
        return self.repo.create(db, city)