CREATE DATABASE IF NOT EXISTS student_portal;
USE student_portal;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    code VARCHAR(20) UNIQUE
);

CREATE TABLE enrollments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
);

-- Students
INSERT INTO students (name, email) VALUES
('Promise Ntandane', 'pntandane72@gmail.com'),
('Thato Makwakwa', 'makwakwa@gmail.com'),
('Lethu Shongwe', 'Lethu7@gmail.com');

-- Courses
INSERT INTO courses (name, code) VALUES
('Database', 'DATA101'),
('Computer Science', 'CS101');