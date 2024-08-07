-- This SQL query retrieves the name and lifespan of each band that plays Glam rock from the 'metal_bands' table.
-- The lifespan is calculated as the number of years the band was active.
-- The results are ordered by lifespan in descending order.

SELECT 
    band_name,  -- Select the name of the band
    (IFNULL(split, 2022) - formed) AS lifespan  -- Calculate the lifespan: if the band has not split, use 2022 as the current year; otherwise, use the split year. Alias the result as 'lifespan'.
FROM 
    metal_bands  -- From the 'metal_bands' table
WHERE 
    style LIKE '%Glam rock%'  -- Filter the results to include only bands with a style that includes 'Glam rock'
ORDER BY 
    lifespan DESC;  -- Order the results by lifespan in descending order
