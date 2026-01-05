import sqlite3

# 1. Connect to a database (it creates the file if it doesn't exist)
connection = sqlite3.connect('automation_journey.db')
cursor = connection.cursor()

# 2. Define the SQL command to create a table
create_table_sql = """
CREATE TABLE IF NOT EXISTS script_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    language TEXT,
    script_name TEXT,
    status TEXT
);
"""

# 3. Execute and Save
cursor.execute(create_table_sql)
connection.commit()

print("Success! Database 'automation_journey.db' created with a 'script_logs' table.")

# 4. Close connection
connection.close()
