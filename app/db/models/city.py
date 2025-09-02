from sqlalchemy import Column,Integer,String,BigInteger,SmallInteger,Text,TIMESTAMP,Numeric,SmallInteger,ForeignKey
from app.db.base import Base

class City(Base):
    __tablename__ = "cities"
    id = Column(BigInteger, primary_key=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    state_id = Column(BigInteger, ForeignKey("states.id"), nullable=False, )
    state_code = Column(String(255),nullable=False)
    country_id = Column(BigInteger, ForeignKey("countries.id"), nullable=False, )
    country_code = Column(String(2),nullable=False)
    latitude = Column(Numeric(10, 8), nullable=False)
    longitude = Column(Numeric(11, 8), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    flag = Column(SmallInteger, nullable=False)
    wikiDataId = Column(String(255), nullable=True)
    
    def __repr__(self):
        return f"<City {self.name}>"
    
    def __str__(self):
        return f"<City {self.name}>"
    
    def __init__(self, name, state_id, state_code, country_id, country_code, latitude, longitude, created_at, updated_at, flag, wikiDataId):
        self.name = name
        self.state_id = state_id
        self.state_code = state_code
        self.country_id = country_id
        self.country_code = country_code
        self.latitude = latitude
        self.longitude = longitude
        self.created_at = created_at
        self.updated_at = updated_at
        self.flag = flag
        self.wikiDataId = wikiDataId
        