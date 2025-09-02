from pydantic import BaseModel
from datetime import datetime

class SubRegionBase(BaseModel):
    id: int
    name: str
    region_id: int | None = None
    translations: str | None = None
    created_at: datetime | None = None
    updated_at: datetime 
    flag: int 
    wikiDataId: str | None = None

class SubRegionCreate(SubRegionBase):
    pass
class SubRegionRead(SubRegionBase):
    id: int
    name: str
    region_id: int | None = None
    translations: str | None = None
    created_at: datetime | None = None
    updated_at: datetime 
    flag: int 
    wikiDataId: str | None = None

class SubRegionUpdate(SubRegionBase):
    id: int
    name: str
    region_id: int | None = None
    translations: str | None = None
    created_at: datetime | None = None
    updated_at: datetime 
    flag: int 
    wikiDataId: str | None = None

class SubRegion(SubRegionBase):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            'id': 'id',
            'name': 'name',
            'region_id': 'region_id',
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
    