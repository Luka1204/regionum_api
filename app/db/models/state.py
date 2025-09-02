from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, SmallInteger,BigInteger,Numeric,ForeignKey
from app.db.base import Base

class State(Base):
    __tablename__ = "states"
    id = Column(BigInteger, nullable=False,primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    country_id = Column(BigInteger, ForeignKey("countries.id"),nullable=False)
    country_code = Column(String(2),nullable=False)
    fips_code = Column(String(255),nullable=True)
    iso2 = Column(String(2),nullable=True)
    type = Column(String(191),nullable=True)
    level = Column(Integer,nullable=True)
    parent_id = Column(Integer,nullable=True)
    latitude = Column(Numeric(10, 8), nullable=True)
    longitude = Column(Numeric(11, 8), nullable=True)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=False)
    flag = Column(SmallInteger, nullable=False)
    wikiDataId = Column(String(255), nullable=True)
    
    def __repr__(self):
        return f"<State {self.name}>"
    
    def __str__(self):
        return f"<State {self.name}>"
    
    def __init__(self, name, country_id, country_code, fips_code, iso2, type, level, parent_id, latitude, longitude,
                 created_at, updated_at, flag, wikiDataId):
        self.name = name
        self.country_id = country_id
        self.country_code = country_code
        self.fips_code = fips_code
        self.iso2 = iso2
        self.type = type
        self.level = level
        self.parent_id = parent_id
        self.latitude = latitude
        self.longitude = longitude
        self.created_at = created_at
        self.updated_at = updated_at
        self.flag = flag
        self.wikiDataId = wikiDataId