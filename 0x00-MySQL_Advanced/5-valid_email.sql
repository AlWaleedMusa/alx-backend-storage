-- This SQL script creates a trigger named 'reset' that is executed before a row in the 'users' table is updated.
-- The purpose of the trigger is to reset the 'valid_email' field to 0 if the email address is changed.

DELIMITER $$  -- Change the delimiter to $$ to allow for the use of semicolons within the trigger definition
CREATE TRIGGER reset
BEFORE UPDATE  -- The trigger is executed before a row is updated in the 'users' table
ON users  -- The trigger is associated with the 'users' table
FOR EACH ROW  -- The trigger is executed for each row that is updated
BEGIN
    IF NEW.email != OLD.email THEN  -- Check if the new email address is different from the old email address
        SET NEW.valid_email = 0;  -- If the email address has changed, set the 'valid_email' field to 0
    END IF;
END $$  -- End of the trigger definition

DELIMITER;  -- Reset the delimiter to the default semicolon
