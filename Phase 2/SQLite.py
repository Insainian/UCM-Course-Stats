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
              VALUES (6, 2, 'CSE 100', 'Fall', '5D')"""
        _conn.execute(sql)

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
              VALUES (100234789, 'Person One', 'personone@example.com')"""
        _conn.execute(sql)

        sql = """INSERT INTO Student (studentID, name, email)
              VALUES (100875939, 'Person Two', 'persontwo@example.com')"""
        _conn.execute(sql)
        sql = """INSERT INTO Student (studentID, name, email)
              VALUES (100130448, 'Person Three', 'personthree@example.com')"""
        _conn.execute(sql)
        sql = """INSERT INTO Student (studentID, name, email)
              VALUES (100566998, 'Person Four', 'personfour@example.com')"""
        _conn.execute(sql)
        sql = """INSERT INTO Student (studentID, name, email)
              VALUES (100556497, 'Person Five', 'personfive@example.com')"""
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
              VALUES (1, 100234789)"""
        _conn.execute(sql)
        sql = """INSERT INTO Enrollment (courseID, studentID)
              VALUES (2, 100234789)"""
        _conn.execute(sql)
        sql = """INSERT INTO Enrollment (courseID, studentID)
              VALUES (3, 100130448)"""
        _conn.execute(sql)
        sql = """INSERT INTO Enrollment (courseID, studentID)
              VALUES (4, 100130448)"""
        _conn.execute(sql)
        sql = """INSERT INTO Enrollment (courseID, studentID)
              VALUES (5, 100130448)"""
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
              VALUES (1, '978-3-16-148415-2')"""
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

        sql = """INSERT INTO Prereq (courseID, prereqID) VALUES (1, 0)"""
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


# ----------- SELECT STATEMENTS ------------

# Select full table statements
def selectAllCourses(_conn):
    print(separator)
    print("Course Table")

    try:
        sql = """SELECT * FROM Course;"""
        cur = _conn.cursor()
        cur.execute(sql)

        formatting = '{:>10} {:>10} {:>10} {:>10} {:>10}'
        heading = formatting.format(
            "courseID", "teacherID", "name", "semester", "section")
        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(
                row[0], row[1], row[2], row[3], row[4]))

    except Error as err:
        print(err)

    print(separator)


def selectTeachers(_conn):
    print(separator)
    print("Teacher Table")

    try:
        sql = """SELECT * FROM Teacher;"""
        cur = _conn.cursor()
        cur.execute(sql)

        formatting = '{:>10} {:>30} {:>10} {:>30} {:>10} {:>10}'
        heading = formatting.format("courseID", "name", "rating", "email", "office", "title")
        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[0], row[1], row[2], row[3], row[4], row[5]))

    except Error as err:
        print(err)

    print(separator)


def selectSchedules(_conn):
    print(separator)
    print("Schedule Table")

    try:
        sql = """SELECT * FROM Schedule;"""
        cur = _conn.cursor()
        cur.execute(sql)

        formatting = '{:>10} {:>10} {:>10} {:>10}'
        heading = formatting.format("courseID", "day", "startTime", "endTime")
        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[0], row[1], row[2], row[3]))

    except Error as err:
        print(err)

    print(separator)


def selectGradeScale(_conn):
    print(separator)
    print("GradeScale Table")

    try:
        sql = """SELECT * FROM GradeScale;"""
        cur = _conn.cursor()
        cur.execute(sql)

        formatting = '{:>10} {:>10} {:>10}'
        heading = formatting.format("courseID", "letterGrade", "minimumScore")
        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[0], row[1], row[2]))

    except Error as err:
        print(err)

    print(separator)


def selectTextbook(_conn):
    print(separator)
    print("GradeScale Table")

    try:
        sql = """SELECT * FROM Textbook;"""
        cur = _conn.cursor()
        cur.execute(sql)

        formatting = '{:>20} {:>20} {:>20}'
        heading = formatting.format("ISBN", "name", "author")
        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[0], row[1], row[2]))

    except Error as err:
        print(err)

    print(separator)


def selectAllStudents(_conn):
    print(separator)
    print("Student Table")

    try:
        sql = """SELECT * FROM Student;"""
        cur = _conn.cursor()
        cur.execute(sql)
        formatting = '{:>10} {:>20} {:>30}'
        heading = formatting.format("studentID", "name", "email")
        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[0], row[1], row[2]))

    except Error as err:
        print(err)

    print(separator)


def selectAllEnrollments(_conn):
    print(separator)
    print("Enrollment Table")

    try:
        sql = """SELECT * FROM Enrollment;"""
        cur = _conn.cursor()
        cur.execute(sql)

        formatting = '{:>10} {:>10}'
        heading = formatting.format("courseID", "studentID")
        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[0], row[1]))

    except Error as err:
        print(err)

    print(separator)


def selectAllCourseTextbooks(_conn):
    print(separator)
    print("CourseTextbook Table")

    try:
        sql = """SELECT * FROM CourseTextbook;"""
        cur = _conn.cursor()
        cur.execute(sql)

        formatting = '{:>10} {:>20}'
        heading = formatting.format("courseID", "ISBN")
        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[0], row[1]))

    except Error as err:
        print(err)

    print(separator)


def selectAllPrereqs(_conn):
    print(separator)
    print("Prereq Table")

    try:
        sql = """SELECT * FROM Prereq;"""
        cur = _conn.cursor()
        cur.execute(sql)

        formatting = '{:>10} {:>10}'
        heading = formatting.format("courseID", "prereqID")
        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[0], row[1]))

    except Error as err:
        print(err)

    print(separator)


def selectAllCoreqs(_conn):
    print(separator)
    print("Coreq Table")

    try:
        sql = """SELECT * FROM Coreq;"""
        cur = _conn.cursor()
        cur.execute(sql)

        formatting = '{:>10} {:>10}'
        heading = formatting.format("courseID", "coreqID")
        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[0], row[1]))

    except Error as err:
        print(err)

    print(separator)


# ---------- STUDENT PERSONAL Schedule ------------
# When visiting the website, the user passes in their studentID.
# The website then allows the student to choose the courses they want enrollment in
def selectPersonalSchedule(_conn, _studentID):
    print(separator)
    print("Student's Personal Schedule")

    try:
        sql = """SELECT  Course.name, Schedule.courseID, Schedule.day,  Schedule.startTime, Schedule.endTime FROM Enrollment 
        JOIN Schedule ON Enrollment.courseID = Schedule.courseID 
        JOIN Course ON Enrollment.courseID = Course.courseID WHERE Enrollment.studentID = ? ORDER BY Enrollment.courseID ASC;"""
        args = [_studentID]
        cur = _conn.cursor()
        cur.execute(sql, args)
        formatting = '{:>10} {:>10} {:>10} {:>10} {:>10}'
        heading = formatting.format("name", "courseID", "day", "startTime", "endTime")
        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[0], row[1], row[2], row[3], row[4]))
    except Error as err:
        print(err)

    print(separator)


def deleteFromPersonalTable(_conn, _studentID, _courseID):
    print(separator)
    print("Delete Course From Personal Schedule")

    try:
        sql = """DELETE FROM Enrollment WHERE studentID = ? AND courseID = ?"""
        args = [_studentID, _courseID]
        _conn.execute(sql, args)

        _conn.commit()
        print("Success")
    except Error as err:
        print(err)

    print(separator)


def addToPersonalTable(_conn, _studentID, _courseID):
    print(separator)
    print("Add Course To Personal Schedule")

    try:
        sql = """INSERT INTO Enrollment (courseID, studentID) VALUES (?, ?);"""
        args = [_courseID, _studentID]
        _conn.execute(sql, args)

        _conn.commit()
        print("Success")
    except Error as err:
        print(err)

    print(separator)


# --------------- SELECT SINGLE COURSE -----------------------
def selectCourseByName(_conn, _name):
    print(separator)
    print("Get Course Info From Course Name")

    try:
        sql = """SELECT * FROM Course WHERE name = ?"""
        args = [_name]
        cur = _conn.cursor()
        cur.execute(sql, args)
        formatting = '{:>10} {:>10} {:>10} {:>10} {:>10}'
        heading = formatting.format(
            "courseID", "teacherID", "name", "semester", "section")

        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[0], row[1], row[2], row[3], row[4]))

    except Error as err:
        print(err)

    print(separator)


def selectCourseById(_conn, _id):
    print(separator)
    print("Get Course Info From Course ID")

    try:
        sql = """SELECT * FROM Course WHERE courseID = ?"""
        args = [_id]
        cur = _conn.cursor()
        cur.execute(sql, args)
        formatting = '{:>10} {:>10} {:>10} {:>10} {:>10}'
        heading = formatting.format(
            "courseID", "teacherID", "name", "semester", "section")

        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[0], row[1], row[2], row[3], row[4]))

    except Error as err:
        print(err)

    print(separator)


# --------------- SELECT COURSE DATA --------------------
def selectCourseTeacher(_conn, _courseID):
    print(separator)
    print("Course's Teacher(s)")

    try:
        sql = """SELECT Teacher.name, Course.name, Course.courseID FROM Course JOIN Teacher ON Course.teacherID = Teacher.teacherID WHERE Course.courseID = ?"""
        args = [_courseID]
        cur = _conn.cursor()
        cur.execute(sql, args)

        formatting = '{:>20} {:>10} {:>10}'
        heading = formatting.format("teacherName", "courseName", "courseID")
        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[0], row[1], row[2]))
    except Error as err:
        print(err)

    print(separator)

def selectTeacherCourse(_conn, _teacherID):
    print(separator)
    print("Courses taught by Teacher")

    try:
        sql = """SELECT Teacher.name, Course.name, Course.courseID FROM Course JOIN Teacher ON Course.teacherID = Teacher.teacherID WHERE Course.teacherID = ?"""
        args = [_teacherID]
        cur = _conn.cursor()
        cur.execute(sql, args)

        formatting = '{:>20} {:>10} {:>10}'
        heading = formatting.format("teacherName", "courseName", "courseID")
        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[0], row[1], row[2]))
    except Error as err:
        print(err)

    print(separator)

def selectCourseTextbook(_conn, _courseID):
    print(separator)
    print("Course's Textbook(s)")

    try:
        sql = """SELECT Course.name, Textbook.name, Textbook.ISBN FROM Course JOIN CourseTextbook ON Course.courseID = CourseTextbook.courseID
         JOIN Textbook ON CourseTextbook.ISBN = Textbook.ISBN WHERE Course.courseID = ?"""
        args = [_courseID]
        cur = _conn.cursor()
        cur.execute(sql, args)

        formatting = '{:>10} {:>20} {:>20}'
        heading = formatting.format("courseName", "textbookName", "ISBN")
        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[0], row[1], row[2]))
    except Error as err:
        print(err)

    print(separator)


def selectGradescaleById(_conn, _id):
    print(separator)
    print("Course's GradeScale")

    try:
        sql = """SELECT * FROM GradeScale WHERE courseID = ?"""
        args = [_id]
        cur = _conn.cursor()
        cur.execute(sql, args)
        formatting = '{:>10} {:>10} {:>10}'
        heading = formatting.format(
            "courseID", "letterGrade", "minimumScore")

        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[0], row[1], row[2]))

    except Error as err:
        print(err)

    print(separator)


def selectScheduleById(_conn, _id):
    print(separator)
    print("Courses's Schedule")

    try:
        sql = """SELECT * FROM Schedule WHERE courseID = ?"""
        args = [_id]
        cur = _conn.cursor()
        cur.execute(sql, args)
        formatting = '{:>10} {:>10} {:>10}'
        heading = formatting.format(
            "day", "startTime", "endTime")

        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[0], row[1], row[2]))

    except Error as err:
        print(err)

    print(separator)


def selectPrereqById(_conn, _id):
    print(separator)
    print("Course's Prereq")

    try:
        sql = """SELECT * FROM Prereq WHERE courseID = ?"""
        args = [_id]
        cur = _conn.cursor()
        cur.execute(sql, args)
        formatting = '{:>10} '
        heading = formatting.format(
            "These are the prereqs required:")

        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[1]))

    except Error as err:
        print(err)

    print(separator)


def selectCoreqById(_conn, _id):
    print(separator)
    print("Course's Coreq")

    try:
        sql = """SELECT * FROM Coreq WHERE courseID = ?"""
        args = [_id]
        cur = _conn.cursor()
        cur.execute(sql, args)
        formatting = '{:>10} '
        heading = formatting.format("These are the coreqs required:")

        print(heading)
        print(separator)

        rows = cur.fetchall()
        for row in rows:
            print(formatting.format(row[1]))

    except Error as err:
        print(err)
    print(separator)


# Create a funciton for each sqlite query we want to do
def main():
    database = r"courses.sql"

    conn = openConnection(database)
    with conn:
    # Call function for querys
    #     dropTables(conn)
    #     createTables(conn)
    #     populateTable(conn)
    #     selectTeachers(conn)
    #     selectSchedules(conn)
    #     selectGradeScale(conn)
    #     selectTextbook(conn)
    #     selectAllStudents(conn)
    #     selectAllEnrollments(conn)
    #     selectAllCourseTextbooks(conn)
    #     selectAllPrereqs(conn)
    #     selectAllCoreqs(conn)
    #     selectPersonalSchedule(conn, 100234789)
    #     deleteFromPersonalTable(conn, 100234789, 3)
    #     selectPersonalSchedule(conn, 100234789)
    #     selectCourseTextbook(conn, 2)
    #     selectCourseByName(conn, "CSE 111")
    #     selectCourseById(conn, 1)
    #     selectCourseTeacher(conn, 1)
    #     selectGradescaleById(conn, 1)
    #     selectScheduleById(conn, 2)
    #     selectPrereqById(conn, 3)
    #     selectCoreqById(conn, 12)
    closeConnection(conn, database)


if __name__ == '__main__':
    main()
