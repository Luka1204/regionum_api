from typing import Optional, List,Iterator
from sqlalchemy import select, func
from sqlalchemy.orm import Session
from app.db.models.city import City
from app.schemas.city import CityCreate, CityUpdate  # si usás Update luego

class CityRepository:

    def get_all(self, db: Session, page: int = 1, items_per_page: int = 10, q: Optional[str] = None) -> List[City]:
        stmt = select(City).order_by(City.id)
        if q:
            stmt = stmt.where(City.name.ilike(f"%{q}%"))
        stmt = stmt.offset((page - 1) * items_per_page).limit(items_per_page)
        return db.execute(stmt).scalars().all()

    def iter_all(self, db: Session, q: Optional[str] = None, chunk_size: int = 1000) -> Iterator[City]:
        stmt = select(City).order_by(City.id)
        if q:
            stmt = stmt.where(City.name.ilike(f"%{q}%"))
        stmt = stmt.execution_options(stream_results=True, yield_per=chunk_size)
        for row in db.execute(stmt).scalars():
            yield row

    @staticmethod
    def count(db: Session, q: Optional[str] = None) -> int:
        stmt = select(func.count()).select_from(City)
        if q:
            stmt = stmt.where(City.name.ilike(f"%{q}%"))
        return db.execute(stmt).scalar_one()
    

    def get_by_id(self, db: Session, city_id: int) -> Optional[City]:
        # API 2.x
        return db.get(City, city_id)
    
    def get_by_name(self, db:Session, city_name:str):
        stmt = select(City).order_by(City.id).where(City.name.ilike(f"%{city_name}%"))
        res = db.execute(stmt).scalars().all()
        return res 
    
    def get_by_state_code(self, db:Session, state_code:str):
        stmt = select(City).order_by(City.id).where(City.state_code == state_code)
        res = db.execute(stmt).scalars().all()
        return res 
    
    def get_by_state_id(self, db:Session, state_id:int):
        stmt = select(City).order_by(City.id).where(City.state_id == state_id)
        res = db.execute(stmt).scalars().all()
        return res 

    def create(self, db: Session, city: CityCreate) -> City:
        # Pydantic v2
        data = city.model_dump()
        obj = City(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

""" from sqlalchemy.orm import Session
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
        return session.execute(query).scalars().all()
    
    def get_by_id(self, db: Session, city_id: int):
        return db.query(City).filter(City.id == city_id).first()
    
    def create(self,db:Session, city:CityCreate):
        db_city = City(**city.dict())
        db.add(db_city)
        db.commit()
        db.refresh(db_city)
        return db_city
     """