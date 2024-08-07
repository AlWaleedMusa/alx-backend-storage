-- This SQL query retrieves the total number of fans for each origin from the 'metal_bands' table.
-- The results are grouped by the 'origin' column and sorted in descending order by the total number of fans.

SELECT origin, SUM(fans) AS nb_fans  -- Select the origin and the sum of fans, aliasing the sum as 'nb_fans'
FROM metal_bands  -- From the 'metal_bands' table
GROUP BY origin  -- Group the results by the 'origin' column
ORDER BY nb_fans DESC;  -- Order the results by the total number of fans in descending order
