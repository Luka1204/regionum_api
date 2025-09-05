from pydantic import BaseModel,ConfigDict
from datetime import datetime

class StateBase(BaseModel):
    id: int
    name: str
    country_id: int | None = None
    country_code: str | None = None
    fips_code: str | None = None
    iso2: str | None = None
    type: str | None = None
    level: int | None = None
    parent_id: int | None = None
    latitude: float | None = None
    longitude: float | None = None
    created_at: datetime | None = None
    updated_at: datetime 
    flag: int 
    wikiDataId: str | None = None

class StateCreate(StateBase):
    pass
class StateRead(StateBase):
    id: int
    name: str
    country_id: int | None = None
    country_code: str | None = None
    fips_code: str | None = None
    iso2: str | None = None
    type: str | None = None
    level: int | None = None
    parent_id: int | None = None # => Puede ser un json que almacene una coll "[{id:1,...},{},{}]" => modificando parent_id, este muta => parent: str | None = None (A futuro)
    latitude: float | None = None
    longitude: float | None = None
    created_at: datetime | None = None
    updated_at: datetime 
    flag: int 
    wikiDataId: str | None = None
    model_config = ConfigDict(from_attributes=True)  # << clave
class StateUpdate(StateBase):
    id: int
    name: str
    country_id: int | None = None
    country_code: str | None = None
    fips_code: str | None = None
    iso2: str | None = None
    type: str | None = None
    level: int | None = None
    parent_id: int | None = None
    latitude: float | None = None
    longitude: float | None = None
    created_at: datetime | None = None
    updated_at: datetime 
    flag: int 
    wikiDataId: str | None = None
class State(StateBase):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            'id': 'id',
            'name': 'name',
            'country_id': 'country_id',
            'country_code': 'country_code',
            'fips_code': 'fips_code',
            'iso2': 'iso2',
            'type': 'type',
            'level': 'level',
            'parent_id': 'parent_id',
            'latitude': 'latitude',
            'longitude': 'longitude',
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
    

