from typing import TypeVar, Generic, Type, Optional, Any
from inventory_service.models.dto.cross_connection import CrossConnectionType
from sqlmodel import SQLModel, Session, select
from fastapi import Depends
from datetime import datetime
from enum import Enum
from ..config.database import get_session

ModelType = TypeVar("ModelType", bound=SQLModel)
EnumType = TypeVar("EnumType", bound=Enum)

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

    async def get_by_datetime_range(
        self,
        start_datetime: datetime,
        end_datetime: datetime,
        timestamp_field: str = "last_mod_ts"
    ) -> list[ModelType]:
        """
        Get records within a datetime range.
        
        Args:
            start_datetime: Start of the datetime range (inclusive)
            end_datetime: End of the datetime range (inclusive)
            timestamp_field: Name of the datetime field to filter on (default: 'last_mod_ts')
            
        Returns:
            List of records that fall within the datetime range
        """
        # Create a select statement
        stmt = select(self.model).where(
            getattr(self.model, timestamp_field) >= start_datetime,
            getattr(self.model, timestamp_field) < end_datetime
        )
        
        # Execute the query
        result = self.session.exec(stmt)
        return result.all()

    async def get_by_datetime_range_and_type(
        self,
        start_datetime: datetime,
        end_datetime: datetime,
        type: EnumType,
        timestamp_field: str = "last_mod_ts",
        type_field: str = "type"
    ) -> list[ModelType]:
        """
        Get records within a datetime range and filtered by type.
        
        Args:
            start_datetime: Start of the datetime range (inclusive)
            end_datetime: End of the datetime range (inclusive)
            type: Enum value to filter by
            timestamp_field: Name of the datetime field to filter on (default: 'last_mod_ts')
            type_field: Name of the type field to filter on (default: 'type')
            
        Returns:
            List of records that fall within the datetime range and match the type
        """
        # Create a select statement
        stmt = select(self.model).where(
            getattr(self.model, timestamp_field) >= start_datetime,
            getattr(self.model, timestamp_field) < end_datetime,
            getattr(self.model, type_field) == type.value
        )
        
        # Execute the query
        result = self.session.exec(stmt)
        return result.all()
    
    async def get_by_id_str(
        self,
        id: str,
        id_field: str = "id"
    ) -> list[ModelType]:
        stmt = select(self.model).where(
            getattr(self.model, id_field) == id,
        )
        result = self.session.exec(stmt)
        return result.all()

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