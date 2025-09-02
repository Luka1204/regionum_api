from sqlalchemy import Column, BigInteger,String,Text, TIMESTAMP, SmallInteger,ForeignKey
from app.db.base import Base

class SubRegion(Base):
    __tablename__="subregions"
    id = Column(BigInteger, primary_key=True, index=True, nullable=False)
    name = Column(String(100),nullable=False)
    translations = Column(Text, nullable=True)
    region_id = Column(BigInteger, ForeignKey("regions.id"),nullable=False)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=False)
    flag = Column(SmallInteger, nullable=False)
    wikiDataId = Column(String(255), nullable=True)
    
    def __repr__(self):
        return f"<SubRegion {self.name}>"   
    
    def __str__(self):
        return f"<SubRegion {self.name}>"
    
    def __init__(self, name, translations, region_id, created_at, updated_at, flag, wikiDataId):    
        self.name = name
        self.translations = translations
        self.region_id = region_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.flag = flag
        self.wikiDataId = wikiDataId
    
    