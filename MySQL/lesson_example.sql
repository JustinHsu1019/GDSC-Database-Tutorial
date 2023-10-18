-- 主題：學生資料管理系統

-- Section 1: CREATE and ALTER Statements

-- 建立新的資料庫
CREATE DATABASE schoolDB;

-- 切換到該資料庫
USE schoolDB;

-- 建立科目資料表
CREATE TABLE subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(50) NOT NULL
);

-- 建立學生資料表
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    subject_id INT,
    grade DECIMAL(4,2),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);

-- 修改學生資料表
ALTER TABLE students ADD COLUMN email VARCHAR(100);

-- Section 2: Basic Query Statements

-- 插入科目資料
INSERT INTO subjects (subject_name) VALUES ('Mathematics'), ('History'), ('Physics');

-- 插入學生資料
INSERT INTO students (first_name, last_name, subject_id, grade, email)
VALUES ('John', 'Doe', 1, 88.5, 'johndoe@gmail.com'),
       ('Jane', 'Smith', 2, 90.0, 'janesmith@gmail.com'),
       ('Robert', 'Johnson', 3, 85.5, 'robertjohnson@gmail.com');

-- 更新學生成績
UPDATE students SET grade = 89.5 WHERE id = 3;

-- 基本查詢語句
SELECT * FROM students;
SELECT first_name, last_name FROM students;

-- 使用 WHERE 子句來過濾資料
SELECT first_name, last_name FROM students WHERE grade > 85;
SELECT first_name, last_name FROM students WHERE subject_id = 2;

-- 資料的排序和分組
SELECT subject_id, COUNT(*) as num_students FROM students GROUP BY subject_id;
SELECT first_name, last_name FROM students ORDER BY grade DESC;

-- Section 3: Advanced Query Techniques

-- JOINs
-- 透過學生和科目資料表的JOIN，查詢學生的名字和他們所修的科目
SELECT s.first_name, s.last_name, sub.subject_name 
FROM students s
INNER JOIN subjects sub ON s.subject_id = sub.id;

-- 子查詢
SELECT 
    s.first_name, 
    s.last_name, 
    sub.subject_name 
FROM students s
INNER JOIN subjects sub ON s.subject_id = sub.id 
WHERE s.grade > (
    SELECT AVG(grade) FROM students
);

-- 建立View
CREATE VIEW view_above_avg_students AS 
SELECT 
    s.first_name, 
    s.last_name, 
    sub.subject_name 
FROM students s
INNER JOIN subjects sub ON s.subject_id = sub.id 
WHERE s.grade > (
    SELECT AVG(grade) FROM students
);

-- 查看View
SELECT * FROM view_above_avg_students;
