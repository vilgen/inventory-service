#!/usr/bin/env python3
"""
Fix INSERT OR REPLACE syntax for PostgreSQL compatibility
"""
import re
from pathlib import Path

def fix_insert_syntax(file_path):
    """Convert INSERT OR REPLACE to PostgreSQL compatible syntax"""
    print(f"Fixing INSERT syntax in {file_path.name}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix "Insert or replace" to "INSERT"
    content = re.sub(r'Insert\s+or\s+replace\s+into', 'INSERT INTO', content, flags=re.IGNORECASE)
    
    # Alternative: Use ON CONFLICT DO NOTHING if you want upsert behavior
    # Uncomment the line below if you want to prevent duplicate key errors
    # content = re.sub(r'INSERT INTO (\w+)', r'INSERT INTO \1', content)
    # content = re.sub(r'(INSERT INTO \w+.*?VALUES.*?)\)', r'\1) ON CONFLICT DO NOTHING', content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Fixed {file_path.name}")

def main():
    """Fix all SQL files"""
    # Fixed path - go up one level from scripts/ to reach data/sql/
    sql_dir = Path(__file__).parent.parent / "data" / "sql"
    
    if not sql_dir.exists():
        print(f"❌ SQL directory not found: {sql_dir}")
        print(f"Current script location: {Path(__file__).parent}")
        print(f"Looking for: {sql_dir}")
        return
    
    sql_files = list(sql_dir.glob("*.sql"))
    if not sql_files:
        print(f"❌ No SQL files found in {sql_dir}")
        return
    
    print(f"📁 Fixing INSERT syntax in {len(sql_files)} files")
    print("-" * 50)
    
    for sql_file in sql_files:
        try:
            fix_insert_syntax(sql_file)
        except Exception as e:
            print(f"❌ Error fixing {sql_file}: {e}")
    
    print(f"\n🎉 Fixed all INSERT statements!")
    print("\nNow try loading again:")
    print("poetry run python -c \"from inventory_service.config.database import init_db; init_db()\"")

if __name__ == '__main__':
    main()