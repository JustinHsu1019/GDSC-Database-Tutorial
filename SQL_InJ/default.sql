CREATE DATABASE ctf_challenge;

USE ctf_challenge;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO users (username, password) VALUES ('admin', 'secure_password123');

CREATE TABLE flags (
    id INT AUTO_INCREMENT PRIMARY KEY,
    flag_content VARCHAR(255) NOT NULL
);

INSERT INTO flags (flag_content) VALUES ('CTF{Simple_SQL_Injection}');
