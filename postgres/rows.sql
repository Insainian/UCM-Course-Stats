INSERT
INTO Course(courseID, teacherID, name, semester, section)
VALUES (1, 1, 'CSE 111', 'Spring', '4D');

INSERT
INTO Course(courseID, teacherID, name, semester, section)
VALUES (2, 2, 'CSE 150', 'Spring', '3D');

INSERT
INTO Course(courseID, teacherID, name, semester, section)
VALUES (6, 2, 'CSE 100', 'Fall', '5D');

INSERT
INTO Course(courseID, teacherID, name, semester, section)
VALUES (3, 3, 'CSE 175', 'Fall', '2D');

INSERT
INTO Course(courseID, teacherID, name, semester, section)
VALUES (4, 4, 'CSE 185', 'Fall', '46');

INSERT
INTO Course(courseID, teacherID, name, semester, section)
VALUES (5, 5, 'CSE 108', 'Spring', '4D');

INSERT
INTO Teacher(teacherID, name, rating, email, office, title)
VALUES (1, 'Derek Sollberger', 5, 'dsollberger@example.com', 'cob 105', 'Professor');

INSERT
INTO Teacher(teacherID, name, rating, email, office, title)
VALUES (2, 'Florin Rusu', 5, 'frusu@exampl.com', 'cob 1', 'Professor');

INSERT
INTO Teacher(teacherID, name, rating, email, office, title)
VALUES (3, 'Angelo Kyrilov', 5, 'akyrilov@example.com', 'tesla', 'Professor');

INSERT
INTO Teacher(teacherID, name, rating, email, office, title)
VALUES (4, 'Sungjin Im', 5, 'sim@example.com', 'NaN', 'Professor');

INSERT
INTO Teacher(teacherID, name, rating, email, office, title)
VALUES (5, 'Santosh Chandrasekhar', 5, 'schandrasekhar@example.com', 'Cob2', 'Professor');

INSERT
INTO Schedule(courseID, day, startTime, endTime)
VALUES (1, 'Monday', '09:00', '10:30');

INSERT
INTO Schedule(courseID, day, startTime, endTime)
VALUES (1, 'Tuesday', '09:00', '10:30');

INSERT
INTO Schedule(courseID, day, startTime, endTime)
VALUES (2, 'Wednesday', '13:00', '14:30');

INSERT
INTO Schedule(courseID, day, startTime, endTime)
VALUES (2, 'Thursday', '13:00', '14:30');

INSERT
INTO Schedule(courseID, day, startTime, endTime)
VALUES (3, 'Friday', '10:30', '13:00');

INSERT
INTO GradeScale(courseID, letterGrade, minimumScore)
VALUES (1, 'A', 90),
       (1, 'B', 80),
       (1, 'C', 70),
       (1, 'D', 60),
       (1, 'F', 50),
       (2, 'A', 89);

INSERT
INTO Textbook(ISBN, name, author)
VALUES ('978-3-16-148410-0', 'Python Programming', 'John Doe');

INSERT
INTO Textbook(ISBN, name, author)
VALUES ('978-3-16-148411-7', 'Advanced Python', 'Jane Smith');

INSERT
INTO Textbook(ISBN, name, author)
VALUES ('978-3-16-148412-4', 'Data Structures', 'Robert Johnson');

INSERT
INTO Textbook(ISBN, name, author)
VALUES ('978-3-16-148414-9', 'Discrete Math', 'Frank John');

INSERT
INTO Textbook(ISBN, name, author)
VALUES ('978-3-16-148415-2', 'Algorithms', 'Jerry Mitt');

INSERT
INTO Student(studentID, name, email)
VALUES (100234789, 'Person One', 'personone@example.com');

INSERT
INTO Student(studentID, name, email)
VALUES (100875939, 'Person Two', 'persontwo@example.com');
INSERT
INTO Student(studentID, name, email)
VALUES (100130448, 'Person Three', 'personthree@example.com');
INSERT
INTO Student(studentID, name, email)
VALUES (100566998, 'Person Four', 'personfour@example.com');
INSERT
INTO Student(studentID, name, email)
VALUES (100556497, 'Person Five', 'personfive@example.com');
INSERT INTO Student (studentid, name, email) VALUES (100999999, 'Sahus Nulu', 'sahusnulu1@gmail.com');

INSERT
INTO Enrollment(courseID, studentID)
VALUES (1, 100234789);

INSERT
INTO Enrollment(courseID, studentID)
VALUES (2, 100234789);

INSERT
INTO Enrollment(courseID, studentID)
VALUES (3, 100130448);

INSERT
INTO Enrollment(courseID, studentID)
VALUES (4, 100130448);

INSERT
INTO Enrollment(courseID, studentID)
VALUES (5, 100130448);

INSERT INTO Enrollment (courseid, studentid) VALUES (4, 100999999);

INSERT INTO Enrollment (courseid, studentid) VALUES (5, 100999999);

INSERT
INTO CourseTextbook(courseID, ISBN)
VALUES (1, '978-3-16-148410-0');

INSERT
INTO CourseTextbook(courseID, ISBN)
VALUES (1, '978-3-16-148415-2');

INSERT
INTO CourseTextbook(courseID, ISBN)
VALUES (2, '978-3-16-148411-7');

INSERT
INTO CourseTextbook(courseID, ISBN)
VALUES (3, '978-3-16-148412-4');

INSERT
INTO CourseTextbook(courseID, ISBN)
VALUES (4, '978-3-16-148414-9');

INSERT
INTO CourseTextbook(courseID, ISBN)
VALUES (5, '978-3-16-148415-2');

INSERT
INTO Prereq(courseID, prereqID)
VALUES (2, 1);

INSERT
INTO Prereq(courseID, prereqID)
VALUES (1, 0);

INSERT
INTO Prereq(courseID, prereqID)
VALUES (3, 1);

INSERT
INTO Prereq(courseID, prereqID)
VALUES (3, 2);

INSERT
INTO Prereq(courseID, prereqID)
VALUES (4, 3);

INSERT
INTO Coreq(courseID, coreqID)
VALUES (5, 6);

INSERT
INTO Coreq(courseID, coreqID)
VALUES (7, 8);

INSERT
INTO Coreq(courseID, coreqID)
VALUES (9, 8);
INSERT
INTO Coreq(courseID, coreqID)
VALUES (10, 11);

INSERT
INTO Coreq(courseID, coreqID)
VALUES (12, 13);
