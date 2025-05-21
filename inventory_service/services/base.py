from typing import TypeVar, Generic, Type, Optional
from sqlmodel import SQLModel, Session
from fastapi import Depends
from ..config.database import get_session

ModelType = TypeVar("ModelType", bound=SQLModel)

class BaseService(Generic[ModelType]):
    """Base class for all services with session management."""
    
    def __init__(self, model: Type[ModelType], session: Session = Depends(get_session)):
        self.model = model
        self.session = session

    async def get(self, id: int) -> Optional[ModelType]:
        """Get a single record by ID."""
        return self.session.get(self.model, id)

    async def get_all(self) -> list[ModelType]:
        """Get all records."""
        return self.session.query(self.model).all()

    async def create(self, obj_in: ModelType) -> ModelType:
        """Create a new record."""
        self.session.add(obj_in)
        self.session.commit()
        self.session.refresh(obj_in)
        return obj_in

    async def update(self, id: int, obj_in: ModelType) -> Optional[ModelType]:
        """Update a record."""
        obj = await self.get(id)
        if obj:
            for key, value in obj_in.dict(exclude_unset=True).items():
                setattr(obj, key, value)
            self.session.commit()
            self.session.refresh(obj)
        return obj

    async def delete(self, id: int) -> bool:
        """Delete a record."""
        obj = await self.get(id)
        if obj:
            self.session.delete(obj)
            self.session.commit()
            return True
        return False 