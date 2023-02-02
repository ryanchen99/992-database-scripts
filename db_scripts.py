import sqlite3
import csv
def setup_courses_table(file):
    # Connect to the database file or create a new one if it doesn't exist
    conn = sqlite3.connect(file)

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create a table in the database
    # Subjects, Number, Name, Credits, Bin_ID
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS COURSE (
            subject TEXT,
            number TEXT,
            name TEXT,
            credit REAL,
            bin_id INTEGER,
            PRIMARY KEY (subject, number, name)
        )
    ''')

    # import courses data
    with open("csv/data.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        
        for row in reader:
            print(row)
            cursor.execute("""
                INSERT INTO COURSE (subject, number, name, credit, bin_id)
                VALUES (?, ?, ?, ?, ?)
            """, row)
    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def setup_bin_table(file):
    # Connect to the database file or create a new one if it doesn't exist
    conn = sqlite3.connect(file)

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create Bin table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS BIN (
            bin_id INTEGER,
            bin_name TEXT,
            PRIMARY KEY (bin_id)
        )
    """)

    # import Bin data
    with open("csv/bin.csv", "r") as file:
        reader = csv.reader(file)
        
        for row in reader:
            print(row)
            cursor.execute("""
                INSERT INTO BIN (bin_id, bin_name)
                VALUES (?, ?)
            """, row)
    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def setup_Specializations_table(file):
    # Connect to the database file or create a new one if it doesn't exist
    conn = sqlite3.connect(file)

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create Bin table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS SPECIALIZATION (
            spec_id INTEGER,
            spec_name TEXT,
            PRIMARY KEY (spec_id)
        )
    """)

    # import Bin data
    with open("csv/spec.csv", "r") as file:
        reader = csv.reader(file)
        
        for row in reader:
            print(row)
            cursor.execute("""
                INSERT INTO SPECIALIZATION (spec_id, spec_name)
                VALUES (?, ?)
            """, row)
    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def setup_CourseToSpec_table(file):
    # Connect to the database file or create a new one if it doesn't exist
    conn = sqlite3.connect(file)

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    cursor.execute("""DROP TABLE IF EXISTS COURSE_TO_SPEC""")    # Create Bin table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS COURSE_TO_SPEC (
            subject TEXT,
            number TEXT,
            name TEXT,
            spec_id INTEGER,
            PRIMARY KEY (subject, number, name, spec_id)
        )
    """)

    # import COURSE_TO_SPEC data
    with open("specialization data/data_with_name.csv", "r") as file:
        reader = csv.reader(file)
        
        for row in reader:
            print(row)
            cursor.execute("""
                INSERT OR IGNORE INTO COURSE_TO_SPEC (subject, number, name, spec_id)
                VALUES (?, ?, ?, ?)
            """, row)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    file = "graduate_tracking_system.db"
    # setup_courses_table(file)
    # setup_bin_table(file)
    # setup_Specializations_table(file)
    setup_CourseToSpec_table(file)