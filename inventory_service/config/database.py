from pydantic_settings import BaseSettings
from typing import Optional
from sqlmodel import SQLModel, create_engine, Session, text
from sqlalchemy.pool import QueuePool
from sqlalchemy.engine import Engine
from inventory_service.schemas.models import (
    InventoryEquipment,
    InventoryCrossConnection,
    InventoryCircuit,
    InventoryCopperService,
    InventoryFttxService,
    InventoryCircuitElement
)
from pathlib import Path
from datetime import datetime

class DatabaseSettings(BaseSettings):
    """Database configuration settings."""
    DB_NAME: str = "inventory.db"
    DB_ECHO: bool = True

    @property
    def DATABASE_URL(self) -> str:
        """Get the SQLite database URL."""
        # Create data directory in the parent directory if it doesn't exist
        data_dir = Path(__file__).parent.parent.parent / "data"
        data_dir.mkdir(exist_ok=True)
        return f"sqlite:///{data_dir}/{self.DB_NAME}"

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

def init_db():
    """Initialize database with SQL scripts."""
    sql_dir = Path(__file__).parent.parent.parent / "data" / "sql"
    
    # Get all SQL files in the directory
    sql_files = sorted(sql_dir.glob("*.sql"))
    
    if not sql_files:
        print("No SQL files found in data/sql directory")
        return
    
    print("Loading SQL scripts...")
    with Session(engine) as session:
        for sql_file in sql_files:
            print(f"Loading {sql_file.name}...")
            try:
                # Read and execute SQL file
                with open(sql_file, 'r') as f:
                    sql_commands = f.read()
                    # Split on semicolons to handle multiple commands
                    for command in sql_commands.split(';'):
                        if command.strip():
                            session.execute(text(command))
                session.commit()
                print(f"Successfully loaded {sql_file.name}")
            except Exception as e:
                print(f"Error loading {sql_file.name}: {str(e)}")
                session.rollback()
                raise
    print("Database initialization completed")

# Dependency to get DB session
def get_session() -> Session:
    """Get database session."""
    with Session(engine) as session:
        yield session 