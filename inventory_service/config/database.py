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
    
    # PostgreSQL settings
    DB_HOST: str = "localhost"
    DB_PORT: int = 5434
    DB_NAME: str = "inventory"
    DB_USER: str = "admin"
    DB_PASSWORD: str = "admin123"
    DB_ECHO: bool = True
    
    # Connection pool settings
    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 20
    DB_POOL_TIMEOUT: int = 30
    DB_POOL_RECYCLE: int = 3600  # 1 hour

    @property
    def DATABASE_URL(self) -> str:
        """Get the PostgreSQL database URL."""
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"


# Create a global instance
db_settings = DatabaseSettings()

# Create SQLModel engine with PostgreSQL optimizations
engine = create_engine(
    db_settings.DATABASE_URL,
    echo=db_settings.DB_ECHO,
    poolclass=QueuePool,
    pool_size=db_settings.DB_POOL_SIZE,
    max_overflow=db_settings.DB_MAX_OVERFLOW,
    pool_timeout=db_settings.DB_POOL_TIMEOUT,
    pool_recycle=db_settings.DB_POOL_RECYCLE,
    # PostgreSQL specific settings
    connect_args={
        "application_name": "inventory_service",
        "connect_timeout": 10,
    }
)


def create_db_and_tables():
    """Create all tables defined in the models."""
    try:
        SQLModel.metadata.create_all(engine)
        print("✅ Database tables created successfully")
    except Exception as e:
        print(f"❌ Error creating database tables: {e}")
        raise


def init_db():
    """Initialize database with SQL scripts."""
    sql_dir = Path(__file__).parent.parent.parent / "data" / "sql"
    
    # Create sql directory if it doesn't exist
    sql_dir.mkdir(parents=True, exist_ok=True)
    
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
                with open(sql_file, 'r', encoding='utf-8') as f:
                    sql_commands = f.read()
                
                # Split on semicolons to handle multiple commands
                # Filter out empty commands and comments
                commands = [
                    cmd.strip() 
                    for cmd in sql_commands.split(';') 
                    if cmd.strip() and not cmd.strip().startswith('--')
                ]
                
                for command in commands:
                    if command:
                        session.execute(text(command))
                
                session.commit()
                print(f"✅ Successfully loaded {sql_file.name}")
                
            except Exception as e:
                print(f"❌ Error loading {sql_file.name}: {str(e)}")
                session.rollback()
                raise

    print("✅ Database initialization completed")


def test_connection():
    """Test the database connection."""
    try:
        with Session(engine) as session:
            result = session.execute(text("SELECT version()"))
            version = result.fetchone()[0]
            print(f"✅ Database connection successful!")
            print(f"PostgreSQL version: {version}")
            return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False


# Dependency to get DB session
def get_session() -> Session:
    """Get database session."""
    with Session(engine) as session:
        yield session


# Alternative async session dependency (if you need async operations)
async def get_async_session() -> Session:
    """Get async database session."""
    with Session(engine) as session:
        yield session


# Health check function
def check_database_health() -> dict:
    """Check database health status."""
    try:
        with Session(engine) as session:
            # Test basic query
            session.execute(text("SELECT 1"))
            
            # Get connection info
            result = session.execute(text("SELECT current_database(), current_user, version()"))
            db_name, user, version = result.fetchone()
            
            return {
                "status": "healthy",
                "database": db_name,
                "user": user,
                "version": version.split()[0] + " " + version.split()[1],
                "timestamp": datetime.now().isoformat()
            }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }