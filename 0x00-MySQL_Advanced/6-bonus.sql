-- This SQL script creates a stored procedure named 'AddBonus' that adds a project and a corresponding correction score for a user.
-- The procedure takes three input parameters:
-- 1. user_id: The ID of the user (INTEGER).
-- 2. project_name: The name of the project (VARCHAR(255)).
-- 3. score: The score for the correction (INTEGER).

DELIMITER $$  -- Change the delimiter to $$ to allow for the use of semicolons within the procedure definition
CREATE PROCEDURE AddBonus(IN user_id INTEGER, IN project_name VARCHAR(255), IN score INTEGER)
BEGIN
    -- Insert the project name into the 'projects' table if it does not already exist
    INSERT INTO projects(name)
    SELECT project_name FROM DUAL
    WHERE NOT EXISTS(SELECT * FROM projects WHERE name = project_name LIMIT 1);

    -- Insert a new correction record into the 'corrections' table
    -- The correction record includes the user_id, the project_id (retrieved based on the project name), and the score
    INSERT INTO corrections(user_id, project_id, score) 
    VALUES (
        user_id,  -- The ID of the user
        (SELECT id FROM projects WHERE name = project_name),  -- The ID of the project, retrieved based on the project name
        score  -- The score for the correction
    ); 
END $$  -- End of the procedure definition
DELIMITER;  -- Reset the delimiter to the default semicolon
