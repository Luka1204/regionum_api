from sqlalchemy import Column,Integer,String,BigInteger,Text,Numeric,TIMESTAMP,SmallInteger,DateTime
from app.db.base import Base

class Country(Base):
    __tablename__= "countries"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(100),nullable=False)
    iso3 = Column(String(3), nullable=True)
    numeric_code = Column(String(3), nullable=True)
    iso2 = Column(String(2),nullable=True)
    phonecode = Column(String(255),nullable=True)
    capital = Column(String(255),nullable=True)
    currency = Column(String(255),nullable=True)
    currency_name = Column(String(255),nullable=True)
    currency_symbol = Column(String(255),nullable=True)
    tld = Column(String(255),nullable=True)
    native = Column(String(255),nullable=True)
    region = Column(String(255),nullable=True)
    region_id = Column(BigInteger,nullable=True,foreign_key="regions.id")
    subregion = Column(String(255),nullable=True)
    subregion_id = Column(BigInteger,nullable=True,foreign_key="subregions.id")
    nationality = Column(String(255), nullable=True)
    timezones = Column(Text,nullable=True)
    translations = Column(Text,nullable=True)
    latitude = Column(Numeric(10, 8), nullable=True)
    longitude = Column(Numeric(11, 8), nullable=True)
    emoji = Column(String(191),nullable=True)
    emojiU = Column(String(191),nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=False)
    flag = Column(SmallInteger,nullable=False)
    wikiDataId = Column(String(255),nullable=True)
    
    def __repr__(self):
        return f"<Country {self.name}>"
    def __str__(self):
        return f"<Country {self.name}>"
    def __init__(self, name, iso3, numeric_code, iso2, phonecode, capital, currency, currency_name, currency_symbol,
                 tld, native, region, region_id, subregion, subregion_id, nationality, timezones, translations,
                 latitude, longitude, emoji, emojiU, created_at, updated_at, flag, wikiDataId):
        self.name = name
        self.iso3 = iso3
        self.numeric_code = numeric_code
        self.iso2 = iso2
        self.phonecode = phonecode
        self.capital = capital
        self.currency = currency
        self.currency_name = currency_name
        self.currency_symbol = currency_symbol
        self.tld = tld
        self.native = native
        self.region = region
        self.region_id = region_id
        self.subregion = subregion
        self.subregion_id = subregion_id
        self.nationality = nationality
        self.timezones = timezones
        self.translations = translations
        self.latitude = latitude
        self.longitude = longitude
        self.emoji = emoji
        self.emojiU = emojiU
        self.created_at = created_at
        self.updated_at = updated_at
        self.flag = flag
        self.wikiDataId = wikiDataId