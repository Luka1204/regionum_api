from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.models.city import City
from app.schemas.city import CityCreate, CityUpdate

class CityRepository:
    def get_all(self,db:Session,page:int):
        
        query = select(City.id).order_by(City.id)
        if page != 0:        
            page_number = page  # Example: current page number
            items_per_page = 10 # Example: number of items per page

            # Calculate the offset
            offset = (page_number - 1) * items_per_page
            #query = db.query(City).all()
            paginated_query = query.limit(items_per_page).offset(offset)
            with db as session:
                results = session.execute(paginated_query).scalars().all()
                if len(results) > 0:
                    return results
        return db.query(City).all()
    
    def get_by_id(self, db: Session, city_id: int):
        return db.query(City).filter(City.id == city_id).first()
    
    def create(self,db:Session, city:CityCreate):
        db_city = City(**city.dict())
        db.add(db_city)
        db.commit()
        db.refresh(db_city)
        return db_city
    