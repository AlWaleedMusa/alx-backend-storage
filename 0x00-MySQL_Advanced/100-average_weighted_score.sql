-- This SQL script creates a stored procedure named 'ComputeAverageWeightedScoreForUser' that calculates and updates the average weighted score for a specific user.
-- The procedure takes one input parameter:
-- 1. user_id: The ID of the user (INT).

DELIMITER $$  -- Change the delimiter to $$ to allow for the use of semicolons within the procedure definition

-- Drop the procedure if it already exists to avoid conflicts
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

-- Create the stored procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    -- Update the 'users' table
    -- Set the 'average_score' field to the average weighted score from the 'corrections' and 'projects' tables for the specified user
    UPDATE users 
    SET average_score = (
        SELECT
            SUM(corrections.score * projects.weight) / SUM(projects.weight)  -- Calculate the weighted average score
        FROM corrections
        INNER JOIN projects ON projects.id = corrections.project_id  -- Join the 'corrections' and 'projects' tables on the project ID
        WHERE corrections.user_id = user_id  -- Filter the results to include only corrections for the specified user
    )
    WHERE users.id = user_id;  -- Only update the user with the specified user_id
END $$  -- End of the procedure definition

DELIMITER;  -- Reset the delimiter to the default semicolon
