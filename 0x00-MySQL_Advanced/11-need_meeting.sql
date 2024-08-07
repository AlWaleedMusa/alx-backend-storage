-- This SQL script drops the view named 'need_meeting' if it already exists.
DROP VIEW IF EXISTS need_meeting;

-- This SQL script creates a view named 'need_meeting'.
-- The view selects the names of students who have a score less than 80
-- and either have never had a meeting or their last meeting was more than one month ago.

CREATE VIEW need_meeting AS 
SELECT 
    name  -- Select the name of the student
FROM 
    students  -- From the 'students' table
WHERE 
    score < 80  -- Where the student's score is less than 80
    AND (students.last_meeting IS NULL  -- And either the student has never had a meeting
    OR students.last_meeting < DATE_ADD(NOW(), INTERVAL -1 MONTH));  -- Or the student's last meeting was more than one month ago
