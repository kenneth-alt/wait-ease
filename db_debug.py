import sqlite3

# Connect to the database
connection = sqlite3.connect('db/queue_app.db')

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Fetch a list of all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Print the contents of each table
for table in tables:
    table_name = table[0]
    print(f"\nTable: {table_name}")
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Close the cursor and the connection
cursor.close()
connection.close()