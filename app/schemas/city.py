from pydantic import BaseModel
from datetime import datetime

class CityBase(BaseModel):
    id: int
    name: str
    state_id: int | None = None
    state_code: str | None = None
    country_id: int | None = None
    country_code: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    created_at: datetime | None = None
    updated_at: datetime 
    flag: int 
    wikiDataId: str | None = None

class CityCreate(CityBase):
    pass
class CityRead(CityBase):
    id: int
    name: str
    state_id: int | None = None
    state_code: str | None = None
    country_id: int | None = None
    country_code: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    created_at: datetime | None = None
    updated_at: datetime 
    flag: int 
    wikiDataId: str | None = None
class CityUpdate(CityBase):
    id: int
    name: str
    state_id: int | None = None
    state_code: str | None = None
    country_id: int | None = None
    country_code: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    created_at: datetime | None = None
    updated_at: datetime 
    flag: int 
    wikiDataId: str | None = None
class City(CityBase):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            'id': 'id',
            'name': 'name',
            'state_id': 'state_id',
            'state_code': 'state_code',
            'country_id': 'country_id',
            'country_code': 'country_code',
            'latitude': 'latitude',
            'longitude': 'longitude',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
            'flag': 'flag',
            'wikiDataId': 'wikiDataId',
        }
        json_encoders = {
            str: lambda v: v,
            int: lambda v: v,
            float: lambda v: v,
            type(None): lambda _: None
        }
    