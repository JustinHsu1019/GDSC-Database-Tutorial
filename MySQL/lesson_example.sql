-- Section 1: CREATE and ALTER Statements

-- 1. Create a new database
CREATE DATABASE schoolDB;
USE schoolDB; -- Switch to the database

-- 2. Create new tables
CREATE TABLE subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(50) NOT NULL
);

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    subject_id INT,
    grade DECIMAL(4,2),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);

-- 3. Modify the table structure
ALTER TABLE students ADD COLUMN email VARCHAR(100);

-- Section 2: Basic Query Statements

-- Inserting some sample data for demo purposes
INSERT INTO subjects (subject_name) VALUES ('Mathematics'), ('History'), ('Physics');

INSERT INTO students (first_name, last_name, subject_id, grade, email)
VALUES ('John', 'Doe', 1, 88.5, 'johndoe@gmail.com'),
       ('Jane', 'Smith', 2, 90.0, 'janesmith@gmail.com'),
       ('Robert', 'Johnson', 3, 85.5, 'robertjohnson@gmail.com');

-- 2. Update existing data
UPDATE students SET grade = 89.5 WHERE id = 3;

-- 1. Basic SELECT statements
SELECT * FROM students;
SELECT first_name, last_name FROM students;

-- 2. Using WHERE clause to filter data
SELECT * FROM students WHERE grade > 85;
SELECT first_name, last_name FROM students WHERE subject_id = 2;

-- 3. Sorting and Grouping data
SELECT subject_id, COUNT(*) as num_students FROM students GROUP BY subject_id;
SELECT first_name, last_name FROM students ORDER BY last_name DESC;

-- Section 3: Advanced Query Techniques

-- 1. Views
CREATE VIEW view_students AS SELECT first_name, last_name, email FROM students WHERE subject_id = 2;
SELECT * FROM view_students;

-- 2. JOINs
-- Note: For a meaningful JOIN, we need another table.
CREATE TABLE clubs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    club_name VARCHAR(50)
);

CREATE TABLE student_clubs (
    student_id INT,
    club_id INT,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (club_id) REFERENCES clubs(id)
);

INSERT INTO clubs (club_name) VALUES ('Chess Club'), ('Science Club'), ('Debate Club');
INSERT INTO student_clubs (student_id, club_id) VALUES (1, 1), (2, 3), (3, 2);

-- Examples for JOIN
SELECT s.first_name, c.club_name 
FROM students s
INNER JOIN student_clubs sc ON s.id = sc.student_id
INNER JOIN clubs c ON sc.club_id = c.id;

-- 3. Sub-queries
SELECT first_name FROM students WHERE subject_id IN (SELECT id FROM subjects WHERE subject_name = 'History');
SELECT first_name FROM students WHERE grade > (SELECT AVG(grade) FROM students);
