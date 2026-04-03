create database physics;
use physics;
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    class INT,
    phone VARCHAR(15),
    join_date DATE,
    status enum('active','inactive')
);
CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    date DATE,
    presence enum('present','absent'),
    FOREIGN KEY (student_id) REFERENCES students(id)
        ON DELETE CASCADE
);
CREATE TABLE marks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    test_name VARCHAR(100),
    marks INT,
    total_marks INT,
    date DATE,
    FOREIGN KEY (student_id) REFERENCES students(id)
        ON DELETE CASCADE
);
CREATE TABLE notices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200),
    description TEXT,
    date DATE
);
CREATE TABLE notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subject VARCHAR(50),
    topic VARCHAR(100),
    pdf_file VARCHAR(255),
    upload_date DATE
);
