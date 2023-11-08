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
        # Create Course
        sql = """CREATE TABLE Course (
                courseID INTEGER PRIMARY KEY AUTOINCREMENT,
                teacherID INTEGER,
                name     VARCHAR NOT NULL,
                semester VARCHAR NOT NULL,
                section  VARCHAR NOT NULL,
                FOREIGN KEY (teacherID) REFERENCES Teacher (teacherID))"""
        _conn.execute(sql)

        # Create Teacher
        sql = """CREATE TABLE Teacher (
                teacherID INTEGER PRIMARY KEY,
                name      VARCHAR NOT NULL,
                rating    REAL,
                email     VARCHAR,
                office    VARCHAR,
                title     VARCHAR)"""
        _conn.execute(sql)

        # Create Schedule
        sql = """CREATE TABLE Schedule (
            courseID  INTEGER,
            day       VARCHAR,
            startTime VARCHAR,
            endTime   VARCHAR,
            PRIMARY KEY (courseID, day),
            FOREIGN KEY (courseID) REFERENCES Course (courseID))"""
        _conn.execute(sql)

        # Create GradeScale
        sql = """CREATE TABLE GradeScale (
                courseID     INTEGER,
                letterGrade  VARCHAR,
                minimumScore REAL,
                PRIMARY KEY (courseID, letterGrade),
                FOREIGN KEY (courseID) REFERENCES Course (courseID))"""
        _conn.execute(sql)

        # Create Textbook
        sql = """CREATE TABLE Textbook (
                ISBN   VARCHAR PRIMARY KEY,
                name   VARCHAR NOT NULL,
                author VARCHAR)"""
        _conn.execute(sql)

        # Create Student
        sql = """CREATE TABLE Student (
                studentID INTEGER PRIMARY KEY,
                name      VARCHAR NOT NULL,
                email     VARCHAR)"""
        _conn.execute(sql)

        # Create Enrollment
        sql = """CREATE TABLE Enrollment (
                courseID  INTEGER,
                studentID INTEGER,
                PRIMARY KEY (courseID, studentID),
                FOREIGN KEY (courseID) REFERENCES Course (courseID),
                FOREIGN KEY (studentID) REFERENCES Student (studentID))"""
        _conn.execute(sql)

        # Create CourseTextbook
        sql = """CREATE TABLE CourseTextbook (
                courseID INTEGER,
                ISBN     VARCHAR,
                PRIMARY KEY (courseID, ISBN),
                FOREIGN KEY (courseID) REFERENCES Course (courseID),
                FOREIGN KEY (ISBN) REFERENCES Textbook (ISBN))"""
        _conn.execute(sql)

        # Create Prereq
        sql = """CREATE TABLE Prereq (
                courseID INTEGER,
                prereqID INTEGER,
                PRIMARY KEY (courseID, prereqID),
                FOREIGN KEY (courseID) REFERENCES Course (courseID),
                FOREIGN KEY (prereqID) REFERENCES Course (courseID))"""
        _conn.execute(sql)

        # Create Coreq
        sql = """CREATE TABLE Coreq (
                courseID INTEGER,
                coreqID  INTEGER,
                PRIMARY KEY (courseID, coreqID),
                FOREIGN KEY (courseID) REFERENCES Course (courseID),
                FOREIGN KEY (coreqID) REFERENCES Course (courseID))"""
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
        # Drop Course
        sql = "DROP TABLE Course"
        _conn.execute(sql)

        # Drop Teacher
        sql = "DROP TABLE Teacher"
        _conn.execute(sql)

        # Drop Schedule
        sql = "DROP TABLE Schedule"
        _conn.execute(sql)

        # Drop GradeScale
        sql = "DROP TABLE GradeScale"
        _conn.execute(sql)

        # Drop Textbook
        sql = "DROP TABLE Textbook"
        _conn.execute(sql)

        # Drop Student
        sql = "DROP TABLE Student"
        _conn.execute(sql)

        # Drop Enrollment
        sql = "DROP TABLE Enrollment"
        _conn.execute(sql)

        # Drop CourseTextbook
        sql = "DROP TABLE CourseTextbook"
        _conn.execute(sql)

        # Drop Prereq
        sql = "DROP TABLE Prereq"
        _conn.execute(sql)

        # Drop Coreq
        sql = "DROP TABLE Coreq"
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
    with conn:
    # Call function for querys
    #     createTables(conn)
    #     dropTables(conn)
    closeConnection(conn, database)


if __name__ == '__main__':
    main()
