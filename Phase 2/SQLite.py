import sqlite3
from sqlite3 import Error

separator = "------------------------------"

def openConnection(_dbFile):
    print(separator)
    print("Open Database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("Connected")

    except Error as err:
        print("Error: ", err)

    print(separator)

    return conn

def closeConnection(_conn, _dbFile):
    print(separator)
    print("Close Database: ", _dbFile)

    try:
        _conn.close()
        print("Closed")
    except Error as err:
        print("Error: ", err)
    print(separator)

def createTables(_conn):
    print(separator)
    print("Create Tables")
    _conn.execute("BEGIN")
    try:
        sql = """CREATE Table Course (
            courseID INTEGER PRIMARY KEY,
            name VARCHAR NOT NULL,
            semester VARCHAR NOT NULL,
            section VARCHAR
            );"""
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("Success")
    except Error as err:
        _conn.execute("ROLLBACK")
        print(err)
    print(separator)
def dropTables(_conn):
    print(separator)
    print("Drop tables")

    _conn.execute("BEGIN")
    try:
        sql = "DROP TABLE Customer"
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("Success")
    except Error as err:
        _conn.execute("ROLLBACK")
        print(err)
    print(separator)

# Create a funciton for each sqlite query we want to do
def main():
    database = r"courses.sql"

    conn = openConnection(database)
    # with conn:
        # Call function for querys

    closeConnection(conn, database)

if __name__ == '__main__':
    main()
