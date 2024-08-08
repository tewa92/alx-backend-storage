-- creates a table users with a unique id, email and name field.

DROP TABLE IF EXISTS users;
CREATE TABLE users (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
email STRING(255) NOT NULL UNIQUE,
name STRING(255)
);
