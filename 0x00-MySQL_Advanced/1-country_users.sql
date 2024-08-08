-- creates a table users with a unique id, email, country and name field.

DROP TABLE IF EXISTS users;
CREATE TABLE users (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
email VARCHAR(255) NOT NULL UNIQUE,
name VARCHAR(255),
country NOT NULL DEFAULT 'US' ENUM('US', 'CO', 'TN')
);
