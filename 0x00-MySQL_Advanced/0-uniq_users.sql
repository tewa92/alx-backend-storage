-- creates a table users with a unique id, email and name field.

DROP TABLE IF EXISTS users;
CREATE TABLE users (
id int() no null auto_increment primary key,
email string(255) not null unique,
name string(255)
);
