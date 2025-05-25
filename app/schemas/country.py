from pydantic import BaseModel
from datetime import datetime

class CountryBase(BaseModel):
    id: int
    name: str
    iso3: str | None = None
    numeric_code: str | None = None
    iso2: str | None = None
    phonecode: str | None = None
    capital: str | None = None
    currency: str | None = None
    currency_name: str | None = None
    currency_symbol: str | None = None
    tld: str | None = None
    native: str | None = None
    region: str | None = None
    region_id: int | None = None
    subregion: str | None = None
    subregion_id: int | None = None
    nationality: str | None = None
    timezones: str | None = None
    translations: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    emoji: str | None = None
    emojiU: str | None = None
    created_at: datetime | None = None
    updated_at: datetime 
    flag: int 
    wikiDataId: str | None = None

class CountryCreate(CountryBase):
    pass
class CountryRead(CountryBase):
    id: int
    name: str
    iso3: str | None = None
    numeric_code: str | None = None
    iso2: str | None = None
    phonecode: str | None = None
    capital: str | None = None
    currency: str | None = None
    currency_name: str | None = None
    currency_symbol: str | None = None
    tld: str | None = None
    native: str | None = None
    region: str | None = None
    region_id: int | None = None
    subregion: str | None = None
    subregion_id: int | None = None
    nationality: str | None = None
    timezones: str | None = None
    translations: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    emoji: str | None = None
    emojiU: str | None = None
    created_at: datetime | None = None
    updated_at: datetime 
    flag: int 
    wikiDataId: str | None = None
class CountryUpdate(CountryBase):
    id: int
    name: str | None = None
    iso3: str | None = None
    numeric_code: str | None = None
    iso2: str | None = None
    phonecode: str | None = None
    capital: str | None = None
    currency: str | None = None
    currency_name: str | None = None
    currency_symbol: str | None = None
    tld: str | None = None
    native: str | None = None
    region: str | None = None
    region_id: int | None = None
    subregion: str | None = None
    subregion_id: int | None = None
    nationality: str | None = None
    timezones: str | None = None
    translations: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    emoji: str | None = None
    emojiU: str | None = None
    created_at: datetime | None = None
    updated_at: datetime 
    flag: int 
    wikiDataId: str | None = None
class Country(CountryBase):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            'id': 'id',
            'name': 'name',
            'iso3': 'iso3',
            'numeric_code': 'numeric_code',
            'iso2': 'iso2',
            'phonecode': 'phonecode',
            'capital': 'capital',
            'currency': 'currency',
            'currency_name': 'currency_name',
            'currency_symbol': 'currency_symbol',
            'tld': 'tld',
            'native': 'native',
            'region': 'region',
            'region_id': 'region_id',
            'subregion': 'subregion',
            'subregion_id': 'subregion_id',
            'nationality': 'nationality',
            'timezones': 'timezones',
            'translations': 'translations',
            'latitude': 'latitude',
            'longitude': 'longitude',
            'emoji': 'emoji',
            'emojiU': 'emojiU',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
            'flag': 'flag',
            'wikiDataId': 'wikiDataId'
        }
        json_encoders = {
            str: lambda v: v,
            int: lambda v: v,
            float: lambda v: v,
            type(None): lambda _: None
        }
    