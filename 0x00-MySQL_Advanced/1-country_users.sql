-- This SQL script creates a table named 'users' if it does not already exist.
-- The table has the following columns:
-- 1. id: An integer that cannot be null, automatically increments with each new record, and serves as the primary key.
-- 2. email: A variable character field with a maximum length of 255 characters, cannot be null, and must be unique.
-- 3. name: A variable character field with a maximum length of 255 characters, which can be null.
-- 4. country: An enumeration field that can only have one of the following values: 'US', 'CO', 'TN'. It cannot be null and defaults to 'US'.

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,  -- Primary key, auto-incrementing integer
    email VARCHAR(255) NOT NULL UNIQUE,  -- Unique email address, cannot be null
    name VARCHAR(255),  -- User's name, can be null
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',  -- Country code, cannot be null, defaults to 'US'
    PRIMARY KEY (id)  -- Primary key constraint on the 'id' column
);
