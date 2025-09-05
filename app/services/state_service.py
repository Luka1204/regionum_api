from typing import Optional, List,Iterator,Any,Dict
from sqlalchemy.orm import Session as SASession
from sqlalchemy import create_engine

from app.services.cache.cache_service import region

from app.repositories.state_repository import StateRepository
from app.schemas.state import StateCreate,StateRead, StateUpdate

class StateService:
    def __init__(self,repo:StateRepository):
        self.repo = repo

    @staticmethod
    @region.cache_on_arguments(namespace="all_states:v1")
    def _list_states_cached(db_url: str, page: int, page_size: int, q: Optional[str]):
        # Este engine solo se crea en cache MISS
        eng = create_engine(db_url, pool_pre_ping=True)
        # Evito colisión con FastAPI Session
        from sqlalchemy.orm import Session as _Sess
        with _Sess(eng) as db:
            rows = StateRepository().get_all(db, page=page, items_per_page=page_size, q=q)
            # Serializamos a dict para que sea cacheable
            return [StateRead.model_validate(r).model_dump() for r in rows]
        
        
    def iter_all_states(self, db: SASession, q: Optional[str] = None, chunk_size: int = 1000) -> Iterator[Dict[str, Any]]:
        for row in self.repo.iter_all(db, q=q, chunk_size=chunk_size):
            yield StateRead.model_validate(row, from_attributes=True).model_dump()

    # Método público que usa la Session y llama al cache
    def list_states(
        self,
        db: SASession,
        page: int = 1,
        page_size: int = 10,
        q: Optional[str] = None,
    ) -> List[StateRead]:
        db_url = db.get_bind().url.render_as_string(hide_password=False)
        data = self._list_states_cached(db_url, page, page_size, q)
        return [StateRead.model_validate(x) for x in data]  # ya son dicts, esto es opcional

    # Invalidación selectiva de una página concreta
    def invalidate_cities(self, db: SASession, page: int, page_size: int, q: Optional[str]):
        db_url = db.get_bind().url.render_as_string(hide_password=False)
        region.invalidate(self._list_states_cached, None, db_url, page, page_size, q)

    """ def list_states(self, db: SASession):
        return self.repo.get_all(db) """
    
    def get_state(self, db: SASession, state_id: int):
        return self.repo.get_by_id(db, state_id)
    
    def create_state(self, db: SASession, state: StateCreate):
        return self.repo.create(db, state)