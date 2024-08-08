-- creates a table users with a unique id, email and name field.

DROP TABLE IF EXISTS users;
CREATE TABLE users (
id INT() NOT NULL AUTO_INCREMENT PRIMARY KEY,
email string(255) NOT NULL UNIQUE,
name string(255)
);
