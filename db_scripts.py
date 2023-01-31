import sqlite3
import csv

# Connect to the database file or create a new one if it doesn't exist
file = "graduate_tracking_system.db"
conn = sqlite3.connect(file)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table in the database
# Subjects, Number, Name, Credits, Bin_ID
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Courses (
        Subjects TEXT,
        Number INTEGER,
        Name TEXT,
        Credits REAL,
        Bin_ID INTEGER,
        PRIMARY KEY (Subjects, Number)
    )
''')

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    
    for row in reader:
        print(row)
        cursor.execute("""
            INSERT INTO Courses (Subjects, Number, Name, Credits, Bin_ID)
            VALUES (?, ?, ?, ?, ?)
        """, row)


# Commit the changes and close the connection
conn.commit()
conn.close()
