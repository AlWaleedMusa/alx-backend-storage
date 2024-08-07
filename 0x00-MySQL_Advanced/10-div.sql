-- This SQL script creates a user-defined function named 'SafeDiv' that performs division safely.
-- The function takes two input parameters:
-- 1. a: The numerator (INT).
-- 2. b: The denominator (INT).
-- The function returns a FLOAT value.
-- If the denominator (b) is zero, the function returns 0 to avoid division by zero errors.
-- Otherwise, it returns the result of the division (a / b).

DELIMITER //  -- Change the delimiter to // to allow for the use of semicolons within the function definition

-- Drop the function if it already exists to avoid conflicts
DROP FUNCTION IF EXISTS SafeDiv;

-- Create the user-defined function
CREATE FUNCTION SafeDiv (
    a INT,  -- The numerator
    b INT   -- The denominator
)
RETURNS FLOAT DETERMINISTIC  -- The function returns a FLOAT and is deterministic (always produces the same result for the same input)
BEGIN
    RETURN (IF (b = 0, 0, a / b));  -- If the denominator is zero, return 0; otherwise, return the result of the division
END //

DELIMITER;  -- Reset the delimiter to the default semicolon
