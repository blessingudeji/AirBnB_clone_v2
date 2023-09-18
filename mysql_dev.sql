-- Create a development database named 'hbnb_dev_db' for the project, if it doesn't already exist.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a MySQL user named 'hbnb_dev' with the password 'hbnb_dev_pwd' if it doesn't exist.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges to the user 'hbnb_dev' on the 'hbnb_dev_db' database.
-- This allows the user to perform all operations on the development database.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Reload the privileges after granting all privileges on the development database.
FLUSH PRIVILEGES;

-- Grant the SELECT privilege to the user 'hbnb_dev' on the database 'performance_schema'.
-- This is necessary for certain internal MySQL operations.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Reload the privileges after granting SELECT privilege.
FLUSH PRIVILEGES;
