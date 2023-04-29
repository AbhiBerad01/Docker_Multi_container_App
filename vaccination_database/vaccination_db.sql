CREATE DATABASE IF NOT EXISTS vaccination_db;
USE vaccination_db;
CREATE TABLE IF NOT EXISTS student (
    reg_no VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    vaccine_status ENUM('Yes', 'No') NOT NULL
);
INSERT INTO student (reg_no, name, vaccine_status)
VALUES
    ('123A',   'John Smith',   'Yes'),
    ('456B',   'Sarah Johnson',   'No'),
    ('789C',   'Michael Lee',   'Yes'),
    ('234D',   'Emily Wilson',   'Yes'),
    ('567E',   'David Chen',   'No'),
    ('890F',   'Jessica Brown',   'No'),
    ('123G',   'Eric Kim',   'Yes'),
    ('456H',   'Rachel Davis',   'No'),
    ('789I',   'Brian Nguyen',   'Yes'),
    ('234J',  'Olivia Taylor',   'Yes');
