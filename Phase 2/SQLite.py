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


# -------- INSERT STATEMENTS ----------
def insertCourseData(_conn):
    print(separator)
    print("Insert Course Data")

    try:
        # Insert data into Course
        sql = """INSERT INTO Course (courseID, teacherID, name, semester, section)
              VALUES (1, 1, 'CSE 111', 'Spring', '4D')"""
        _conn.execute(sql)

        sql = """INSERT INTO Course (courseID, teacherID, name, semester, section)
              VALUES (2, 2, 'CSE 150', 'Spring', '3D')"""
        _conn.execute(sql)
        sql = """INSERT INTO Course (courseID, teacherID, name, semester, section)
              VALUES (3, 3, 'CSE 175', 'Fall', '2D')"""
        _conn.execute(sql)
        sql = """INSERT INTO Course (courseID, teacherID, name, semester, section)
              VALUES (4, 4, 'CSE 185', 'Fall', '46')"""
        _conn.execute(sql)
        sql = """INSERT INTO Course (courseID, teacherID, name, semester, section)
              VALUES (5, 5, 'CSE 108', 'Spring', '4D')"""
        _conn.execute(sql)

        print("Success")
    except Error as err:
        print("Error: ", err)

    print(separator)

def insertTeacherData(_conn):
    print(separator)
    print("Insert Teacher Data")

    try:
        # Insert data into Teacher
        sql = """INSERT INTO Teacher (teacherID, name, rating, email, office, title)
               VALUES (1, 'Derek Sollberger', 5, 'dsollberger@example.com', 'cob 105', 'Professor')"""
        _conn.execute(sql)
        sql = """INSERT INTO Teacher (teacherID, name, rating, email, office, title)
               VALUES (2, 'Florin Rusu', 5, 'frusu@exampl.com', 'cob 1', 'Professor')"""
        _conn.execute(sql)
        sql = """INSERT INTO Teacher (teacherID, name, rating, email, office, title)
               VALUES (3, 'Angelo Kyrilov', 5, 'akyrilov@example.com', 'tesla', 'Professor')"""
        _conn.execute(sql)
        sql = """INSERT INTO Teacher (teacherID, name, rating, email, office, title)
               VALUES (4, 'Sungjin Im', 5, 'sim@example.com', 'NaN', 'Professor')"""
        _conn.execute(sql)
        sql = """INSERT INTO Teacher (teacherID, name, rating, email, office, title)
               VALUES (5, 'Santosh Chandrasekhar', 5, 'schandrasekhar@example.com', 'Cob2', 'Professor')"""
        _conn.execute(sql)

        print("Success")
    except Error as err:
        print("Error: ", err)

    print(separator)

def insertScheduleData(_conn):
    print(separator)
    print("Insert Schedule Data")

    try:
        # Insert data into Schedule
        sql = """INSERT INTO Schedule (courseID, day, startTime, endTime)
              VALUES (1, 'Monday', '09:00', '10:30')"""
        _conn.execute(sql)

        sql = """INSERT INTO Schedule (courseID, day, startTime, endTime) VALUES (1, 'Tuesday', '09:00', '10:30')"""
        _conn.execute(sql)

        sql = """INSERT INTO Schedule (courseID, day, startTime, endTime) VALUES (2, 'Wednesday', '13:00', '14:30')"""
        _conn.execute(sql)

        sql = """INSERT INTO Schedule (courseID, day, startTime, endTime) VALUES (2, 'Thursday', '13:00', '14:30')"""
        _conn.execute(sql)

        sql = """INSERT INTO Schedule (courseID, day, startTime, endTime) VALUES (3, 'Friday', '10:30', '13:00')"""
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("Success")
    except Error as err:
        print("Error: ", err)

    print(separator)

def insertGradeScaleData(_conn):
    print(separator)
    print("Insert GradeScale Data")

    try:
        # Insert data into GradeScale
        sql = """INSERT INTO GradeScale (courseID, letterGrade, minimumScore)
                VALUES (1, 'A', 90),
                       (1, 'B', 80),
                       (1, 'C', 70),
                       (1, 'D', 60),
                       (1, 'F', 50),
                       (2, 'A', 89)"""
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("Success")
    except Error as err:
        print("Error: ", err)

    print(separator)

def insertTextbookData(_conn):
    print(separator)
    print("Insert Textbook Data")

    try:
        # Insert data into Textbook
        sql = """        INSERT INTO Textbook (ISBN, name, author) VALUES ('978-3-16-148410-0', 'Python Programming', 'John Doe')"""
        _conn.execute(sql)

        sql = """INSERT INTO Textbook (ISBN, name, author) VALUES ('978-3-16-148411-7', 'Advanced Python', 'Jane Smith')"""
        _conn.execute(sql)

        sql = """INSERT INTO Textbook (ISBN, name, author) VALUES ('978-3-16-148412-4', 'Data Structures', 'Robert Johnson')"""
        _conn.execute(sql)

        sql = """INSERT INTO Textbook (ISBN, name, author) VALUES ('978-3-16-148414-9', 'Discrete Math', 'Frank John')"""
        _conn.execute(sql)

        sql = """INSERT INTO Textbook (ISBN, name, author) VALUES ('978-3-16-148415-2', 'Algorithms', 'Jerry Mitt')"""
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("Success")
    except Error as err:
        print("Error: ", err)

    print(separator)

def insertStudentData(_conn):
    print(separator)
    print("Insert Student Data")

    try:
        # Insert data into Student
        sql = """INSERT INTO Student (studentID, name, email)
              VALUES (1, 'Person One', 'personone@example.com')"""
        _conn.execute(sql)

        sql = """INSERT INTO Student (studentID, name, email)
              VALUES (2, 'Person Two', 'persontwo@example.com')"""
        _conn.execute(sql)
        sql = """INSERT INTO Student (studentID, name, email)
              VALUES (3, 'Person Three', 'personthree@example.com')"""
        _conn.execute(sql)
        sql = """INSERT INTO Student (studentID, name, email)
              VALUES (4, 'Person Four', 'personfour@example.com')"""
        _conn.execute(sql)
        sql = """INSERT INTO Student (studentID, name, email)
              VALUES (5, 'Person Five', 'personfive@example.com')"""
        _conn.execute(sql)

        print("Success")
    except Error as err:
        print("Error: ", err)

    print(separator)


def insertEnrollmentData(_conn):
    print(separator)
    print("Insert Enrollment Data")

    try:
        # Insert data into Enrollment
        sql = """INSERT INTO Enrollment (courseID, studentID)
              VALUES (1, 1)"""
        _conn.execute(sql)
        sql = """INSERT INTO Enrollment (courseID, studentID)
              VALUES (2, 2)"""
        _conn.execute(sql)
        sql = """INSERT INTO Enrollment (courseID, studentID)
              VALUES (3, 3)"""
        _conn.execute(sql)
        sql = """INSERT INTO Enrollment (courseID, studentID)
              VALUES (4, 4)"""
        _conn.execute(sql)
        sql = """INSERT INTO Enrollment (courseID, studentID)
              VALUES (5, 5)"""
        _conn.execute(sql)

        print("Success")
    except Error as err:
        print("Error: ", err)

    print(separator)

def insertCourseTextbookData(_conn):
    print(separator)
    print("Insert CourseTextbook Data")

    try:
        # Insert data into CourseTextbook
        sql = """INSERT INTO CourseTextbook (courseID, ISBN)
              VALUES (1, '978-3-16-148410-0')"""
        _conn.execute(sql)
        sql = """INSERT INTO CourseTextbook (courseID, ISBN)
              VALUES (2, '978-3-16-148411-7')"""
        _conn.execute(sql)
        sql = """INSERT INTO CourseTextbook (courseID, ISBN)
              VALUES (3, '978-3-16-148412-4')"""
        _conn.execute(sql)
        sql = """INSERT INTO CourseTextbook (courseID, ISBN)
              VALUES (4, '978-3-16-148414-9')"""
        _conn.execute(sql)
        sql = """INSERT INTO CourseTextbook (courseID, ISBN)
              VALUES (5, '978-3-16-148415-2')"""
        _conn.execute(sql)

        print("Success")
    except Error as err:
        print("Error: ", err)

    print(separator)

def insertPrereqData(_conn):
    print(separator)
    print("Insert Prereq Data")

    try:
        # Insert data into Prereq
        sql = """INSERT INTO Prereq (courseID, prereqID)
              VALUES (2, 1)"""
        _conn.execute(sql)

        sql = """INSERT INTO Prereq (courseID, prereqID) VALUES (1, null)"""
        _conn.execute(sql)

        sql = """INSERT INTO Prereq (courseID, prereqID) VALUES (3, 1)"""
        _conn.execute(sql)

        sql = """INSERT INTO Prereq (courseID, prereqID) VALUES (3, 2)"""
        _conn.execute(sql)

        sql = """INSERT INTO Prereq (courseID, prereqID) VALUES (4, 3)"""
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("Success")
    except Error as err:
        print("Error: ", err)

    print(separator)

def insertCoreqData(_conn):
    print(separator)
    print("Insert Coreq Data")

    try:
        # Insert data into Coreq
        sql = """INSERT INTO Coreq (courseID, coreqID) VALUES (5, 6)"""
        _conn.execute(sql)

        sql = """INSERT INTO Coreq (courseID, coreqID) VALUES (7, 8)"""
        _conn.execute(sql)

        sql = """INSERT INTO Coreq (courseID, coreqID) VALUES (9, 8)"""
        _conn.execute(sql)
        sql = """INSERT INTO Coreq (courseID, coreqID) VALUES (10, 11)"""
        _conn.execute(sql)

        sql = """INSERT INTO Coreq (courseID, coreqID) VALUES (12, 13)"""
        _conn.execute(sql)

        _conn.execute("COMMIT")
        print("Success")
    except Error as err:
        print("Error: ", err)

    print(separator)

def populateTable(_conn):
    insertCourseData(_conn)
    insertTeacherData(_conn)
    insertScheduleData(_conn)
    insertGradeScaleData(_conn)
    insertTextbookData(_conn)
    insertStudentData(_conn)
    insertEnrollmentData(_conn)
    insertCourseTextbookData(_conn)
    insertPrereqData(_conn)
    insertCoreqData(_conn)

# Create a funciton for each sqlite query we want to do
def main():
    database = r"courses.sql"

    conn = openConnection(database)
    # with conn:
    # Call function for querys
    #     createTables(conn)
    #     dropTables(conn)
    #     populateTable(conn)
    closeConnection(conn, database)


if __name__ == '__main__':
    main()
