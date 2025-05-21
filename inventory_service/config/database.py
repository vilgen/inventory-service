from pydantic_settings import BaseSettings
from typing import Optional
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.pool import QueuePool
from inventory_service.schemas.models import (
    InventoryEquipment,
    InventoryCrossConnection,
    InventoryCircuit,
    InventoryCopperService,
    InventoryFttxService
)
import os

class DatabaseSettings(BaseSettings):
    """Database configuration settings."""
    DB_NAME: str = "inventory.db"
    DB_ECHO: bool = True

    @property
    def DATABASE_URL(self) -> str:
        """Get the SQLite database URL."""
        # Create data directory if it doesn't exist
        os.makedirs("data", exist_ok=True)
        return f"sqlite:///data/{self.DB_NAME}"

    class Config:
        env_file = ".env"
        case_sensitive = True

# Create a global instance
db_settings = DatabaseSettings()

# Create SQLModel engine
engine = create_engine(
    db_settings.DATABASE_URL,
    echo=db_settings.DB_ECHO,
    connect_args={"check_same_thread": False}  # Needed for SQLite
)

# Create all tables
def create_db_and_tables():
    """Create all tables defined in the models."""
    SQLModel.metadata.create_all(engine)

# Dependency to get DB session
def get_session():
    """Get database session."""
    with Session(engine) as session:
        yield session 