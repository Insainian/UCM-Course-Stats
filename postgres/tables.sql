CREATE TABLE Course
(
    courseID  SERIAL PRIMARY KEY,
    teacherID INTEGER,
    name      VARCHAR NOT NULL,
    semester  VARCHAR NOT NULL,
    section   VARCHAR NOT NULL,
    FOREIGN KEY (teacherID) REFERENCES Teacher (teacherID)
);

CREATE TABLE Teacher
(
    teacherID INTEGER PRIMARY KEY,
    name      VARCHAR NOT NULL,
    rating    REAL,
    email     VARCHAR,
    office    VARCHAR,
    title     VARCHAR
);

CREATE TABLE Schedule
(
    courseID  INTEGER,
    day       VARCHAR,
    startTime VARCHAR,
    endTime   VARCHAR,
    PRIMARY KEY (courseID, day),
    FOREIGN KEY (courseID) REFERENCES Course (courseID)
);

CREATE TABLE GradeScale
(
    courseID     INTEGER,
    letterGrade  VARCHAR,
    minimumScore REAL,
    PRIMARY KEY (courseID, letterGrade),
    FOREIGN KEY (courseID) REFERENCES Course (courseID)
);

CREATE TABLE Textbook
(
    ISBN   VARCHAR PRIMARY KEY,
    name   VARCHAR NOT NULL,
    author VARCHAR
);

CREATE TABLE Student
(
    studentID INTEGER PRIMARY KEY,
    name      VARCHAR NOT NULL,
    email     VARCHAR
);

CREATE TABLE Enrollment
(
    courseID  INTEGER,
    studentID INTEGER,
    PRIMARY KEY (courseID, studentID),
    FOREIGN KEY (courseID) REFERENCES Course (courseID),
    FOREIGN KEY (studentID) REFERENCES Student (studentID)
);

CREATE TABLE CourseTextbook
(
    courseID INTEGER,
    ISBN     VARCHAR,
    PRIMARY KEY (courseID, ISBN),
    FOREIGN KEY (courseID) REFERENCES Course (courseID),
    FOREIGN KEY (ISBN) REFERENCES Textbook (ISBN)
);

CREATE TABLE Prereq
(
    courseID INTEGER,
    prereqID INTEGER,
    PRIMARY KEY (courseID, prereqID),
    FOREIGN KEY (courseID) REFERENCES Course (courseID),
    FOREIGN KEY (prereqID) REFERENCES Course (courseID)
);

CREATE TABLE Coreq
(
    courseID INTEGER,
    coreqID  INTEGER,
    PRIMARY KEY (courseID, coreqID),
    FOREIGN KEY (courseID) REFERENCES Course (courseID),
    FOREIGN KEY (coreqID) REFERENCES Course (courseID)
);