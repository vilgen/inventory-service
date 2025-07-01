# test_connection.py
from sqlalchemy import create_engine, text

# Use the port you configured (5432 or 5433)
DATABASE_URL = "postgresql://admin:admin123@localhost:5433/inventory"  # Adjust port if needed
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version()"))
        print("✅ Docker PostgreSQL connection successful!")
        print("Version:", result.fetchone()[0])
        
        # Test database
        result = connection.execute(text("SELECT current_database()"))
        print("Database:", result.fetchone()[0])
        
except Exception as e:
    print(f"❌ Connection failed: {e}")