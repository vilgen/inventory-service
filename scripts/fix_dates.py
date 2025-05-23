import re
from datetime import datetime
from pathlib import Path

def convert_oracle_date(match):
    date_str = match.group(1)
    try:
        # Parse the Oracle date format (DD-MON-RR)
        date_obj = datetime.strptime(date_str, '%d-%b-%y')
        # Convert to SQLite datetime string format (YYYY-MM-DD HH:MM:SS)
        return f"'{date_obj.strftime('%Y-%m-%d %H:%M:%S')}'"
    except ValueError as e:
        print(f"Error converting date {date_str}: {e}")
        return match.group(0)  # Return original if conversion fails

def fix_dates_in_file(file_path):
    # Read the file
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Pattern to match to_date('DD-MON-RR','DD-MON-RR')
    pattern = r"to_date\('(\d{2}-[A-Z]{3}-\d{2})','DD-MON-RR'\)"
    
    # Replace all occurrences
    modified_content = re.sub(pattern, convert_oracle_date, content)
    
    # Write back to file
    with open(file_path, 'w') as f:
        f.write(modified_content)

def fix_colon_bind(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # First fix any double colons in datetime strings
    datetime_pattern = r"'(\d{4}-\d{2}-\d{2} \d{2})::(\d{2}:\d{2})'"
    content = re.sub(datetime_pattern, r"'\1:\2'", content)
    
    # Now handle colons in identifiers (like FR# :4)
    # Pattern looks for : followed by numbers, but not in IP addresses or other special contexts
    colon_pattern = r"'([^']*?)(?<!\.)(?<!:)(?<!\d):(\d+)([^']*?)'"
    
    def replace_colon(match):
        prefix = match.group(1)
        number = match.group(2)
        suffix = match.group(3)
        # Only replace if it's not part of a datetime string
        if not re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', f"{prefix}:{number}{suffix}"):
            return f"'{prefix}::{number}{suffix}'"
        return match.group(0)
    
    # Replace colons in identifiers
    content = re.sub(colon_pattern, replace_colon, content)
    
    with open(file_path, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    sql_dir = Path(__file__).parent.parent / "data" / "sql"
    for sql_file in sql_dir.glob("*.sql"):
        print(f"Processing {sql_file}...")
        fix_dates_in_file(sql_file)
        fix_colon_bind(sql_file)
    print("Done!") 