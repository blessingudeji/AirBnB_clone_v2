-- Create a database named 'hbnb_test_db' for project testing, if it doesn't already exist.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a MySQL user named 'hbnb_test' with the password 'hbnb_test_pwd' if it doesn't exist.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant the SELECT privilege to the user 'hbnb_test' on the database 'performance_schema'.
-- This is necessary for certain internal MySQL operations.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Reload the privileges after granting SELECT privilege.
FLUSH PRIVILEGES;

-- Grant all privileges to the user 'hbnb_test' on the 'hbnb_test_db' database.
-- This allows the user to perform all operations on the testing database.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Reload the privileges after granting all privileges on the testing database.
FLUSH PRIVILEGES;
