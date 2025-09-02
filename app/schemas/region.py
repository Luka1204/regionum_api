from pydantic import BaseModel
from datetime import datetime

class RegionBase(BaseModel):
    id: int
    name: str
    translations: str | None = None
    created_at: datetime | None = None
    updated_at: datetime 
    flag: int 
    wikiDataId: str | None = None
    

class RegionCreate(RegionBase):
    pass
class RegionRead(RegionBase):
    id: int
    name: str
    translations: str | None = None
    created_at: datetime | None = None
    updated_at: datetime 
    flag: int 
    wikiDataId: str | None = None
class RegionUpdate(RegionBase):
    id: int
    name: str
    translations: str | None = None
    created_at: datetime | None = None
    updated_at: datetime 
    flag: int 
    wikiDataId: str | None = None
class Region(RegionBase):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            'id': 'id',
            'name': 'name',
            'timezones': 'timezones',
            'translations': 'translations',
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
    