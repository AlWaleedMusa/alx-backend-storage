-- This SQL script creates a stored procedure named 'ComputeAverageScoreForUser' that calculates and updates the average score for a specific user.
-- The procedure takes one input parameter:
-- 1. user_id: The ID of the user (INT).

DELIMITER $$  -- Change the delimiter to $$ to allow for the use of semicolons within the procedure definition

-- Drop the procedure if it already exists to avoid conflicts
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Create the stored procedure
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    -- Update the 'users' table
    -- Set the 'average_score' field to the average score from the 'corrections' table for the specified user
    UPDATE users
    SET
        average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
    WHERE id = user_id;  -- Only update the user with the specified user_id
END $$  -- End of the procedure definition

DELIMITER;  -- Reset the delimiter to the default semicolon
