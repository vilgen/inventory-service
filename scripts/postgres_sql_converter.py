#!/usr/bin/env python3
"""
Convert Oracle SQL export files to PostgreSQL compatible format
"""
import re
from pathlib import Path


# Mapping from SQL file names to PostgreSQL table names
FILE_TO_TABLE_MAP = {
    'circ_elem_export.sql': 'inventory_circuit_element',
    'circuit_export.sql': 'inventory_circuit', 
    'copper_export.sql': 'inventory_copper_service',
    'cross_conn_export.sql': 'inventory_cross_connection',
    'equipment_export.sql': 'inventory_equipment',
    'fttx_export.sql': 'inventory_fttx_service'
}


def convert_sql_to_postgresql(file_path):
    """Convert Oracle SQL file to PostgreSQL format"""
    print(f"Converting {file_path} to PostgreSQL format...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get the correct table name
    file_name = file_path.name
    table_name = FILE_TO_TABLE_MAP.get(file_name, 'unknown_table')
    
    # 1. Replace Oracle-specific syntax
    content = re.sub(r'REM INSERTING.*\n', '', content)  # Remove Oracle comments
    content = re.sub(r'SET DEFINE OFF;\n', '', content)  # Remove Oracle commands
    
    # 2. Fix INSERT statements
    content = re.sub(r'Insert into EXPORT_TABLE', f'INSERT INTO {table_name}', content, flags=re.IGNORECASE)
    content = re.sub(r'insert into EXPORT_TABLE', f'INSERT INTO {table_name}', content, flags=re.IGNORECASE)
    
    # 3. Fix NULL values
    content = re.sub(r"'null'", 'NULL', content, flags=re.IGNORECASE)
    content = re.sub(r'"null"', 'NULL', content, flags=re.IGNORECASE)
    
    # 4. Fix empty strings to NULL for optional fields
    content = re.sub(r"''", 'NULL', content)
    
    # 5. Fix Oracle DUAL table references (if any)
    content = re.sub(r'FROM DUAL', '', content, flags=re.IGNORECASE)
    
    # 6. Add proper statement terminators
    lines = content.split('\n')
    new_lines = []
    
    for line in lines:
        line = line.strip()
        if line and not line.endswith(';') and line.startswith('INSERT'):
            line += ';'
        if line:
            new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    # 7. Add transaction wrapper for safety
    final_content = f"""-- PostgreSQL data import for {table_name}
-- Converted from Oracle export: {file_name}

BEGIN;

{content}

COMMIT;
"""
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"✅ Converted {file_path} -> {table_name}")


def validate_sql_syntax(file_path):
    """Basic validation of SQL syntax"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # Check for common issues
    if 'EXPORT_TABLE' in content:
        issues.append("Still contains EXPORT_TABLE references")
    
    if 'to_date(' in content.lower():
        issues.append("Contains Oracle to_date() functions")
    
    if "REM INSERTING" in content:
        issues.append("Contains Oracle comments")
    
    # Count INSERT statements
    insert_count = len(re.findall(r'INSERT INTO', content, re.IGNORECASE))
    
    return {
        'file': file_path.name,
        'issues': issues,
        'insert_count': insert_count,
        'valid': len(issues) == 0
    }


def main():
    """Main conversion process"""
    sql_dir = Path(__file__).parent.parent / "data" / "sql"
    
    if not sql_dir.exists():
        print(f"❌ SQL directory not found: {sql_dir}")
        return
    
    sql_files = list(sql_dir.glob("*.sql"))
    if not sql_files:
        print(f"❌ No SQL files found in {sql_dir}")
        return
    
    print(f"📁 Found {len(sql_files)} SQL files to convert")
    print("-" * 50)
    
    results = []
    
    for sql_file in sql_files:
        try:
            # Convert the file
            convert_sql_to_postgresql(sql_file)
            
            # Validate the result
            validation = validate_sql_syntax(sql_file)
            results.append(validation)
            
        except Exception as e:
            print(f"❌ Error processing {sql_file}: {e}")
            results.append({
                'file': sql_file.name,
                'issues': [f"Conversion error: {e}"],
                'insert_count': 0,
                'valid': False
            })
    
    # Print summary
    print("\n" + "=" * 50)
    print("CONVERSION SUMMARY")
    print("=" * 50)
    
    total_inserts = 0
    valid_files = 0
    
    for result in results:
        status = "✅ VALID" if result['valid'] else "❌ ISSUES"
        print(f"{status} {result['file']} - {result['insert_count']} INSERT statements")
        
        if result['issues']:
            for issue in result['issues']:
                print(f"  ⚠️  {issue}")
        
        total_inserts += result['insert_count']
        if result['valid']:
            valid_files += 1
    
    print(f"\n📊 Total: {valid_files}/{len(results)} files valid, {total_inserts} INSERT statements")
    
    if valid_files == len(results):
        print("\n🎉 All files converted successfully!")
        print("\nNext steps:")
        print("1. Run: poetry run python -c \"from inventory_service.config.database import init_db; init_db()\"")
        print("2. Check data: poetry run python -c \"from inventory_service.config.database import engine; from sqlalchemy import text; from sqlalchemy.orm import Session; session = Session(engine); print('Copper services:', session.execute(text('SELECT COUNT(*) FROM inventory_copper_service')).scalar())\"")
    else:
        print(f"\n⚠️  {len(results) - valid_files} files need manual review")


if __name__ == '__main__':
    main()