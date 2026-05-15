import sqlite3

connection = sqlite3.connect("database/trips.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS trips (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    student_name TEXT,

    city TEXT,

    days INTEGER,

    budget INTEGER,

    travel_style TEXT,

    total_cost INTEGER
)
""")

connection.commit()
connection.close()

print("Database Created Successfully")