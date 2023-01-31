def setup_courses_table(file):
    import sqlite3
    import csv

    # Connect to the database file or create a new one if it doesn't exist
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

    # import courses data
    with open("csv/data.csv", "r") as file:
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

def setup_bin_table(file):
    import sqlite3
    import csv

    # Connect to the database file or create a new one if it doesn't exist
    conn = sqlite3.connect(file)

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create Bin table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Bin (
            Bin_ID INTEGER,
            Bin_Name TEXT,
            PRIMARY KEY (Bin_ID)
        )
    """)

    # import Bin data
    with open("csv/bin.csv", "r") as file:
        reader = csv.reader(file)
        
        for row in reader:
            print(row)
            cursor.execute("""
                INSERT INTO Bin (Bin_ID, Bin_Name)
                VALUES (?, ?)
            """, row)
    # Commit the changes and close the connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    file = "graduate_tracking_system.db"
    setup_courses_table(file)
    setup_bin_table(file)