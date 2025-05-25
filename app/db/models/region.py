from sqlalchemy import Column,BigInteger,String,Text,TIMESTAMP,SmallInteger
from app.db.base import Base

class Region(Base):
    __tablename__ = "regions"
    id = Column(BigInteger, primary_key=True, index=True, nullable=False)
    name = Column(String(100), nullable=False)
    translations = Column(Text, nullable=True)
    code = Column(String(10), nullable=True)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=False)
    flag = Column(SmallInteger, nullable=False)
    wikiDataId = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<Region {self.name}>"

    def __str__(self):
        return f"<Region {self.name}>"

    def __init__(self, name, translations, created_at, updated_at, flag, wikiDataId):
        self.name = name
        self.translations = translations
        self.created_at = created_at
        self.updated_at = updated_at
        self.flag = flag
        self.wikiDataId = wikiDataId