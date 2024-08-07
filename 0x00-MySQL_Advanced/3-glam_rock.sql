-- This SQL query calculates the lifespan of each band from the 'metal_bands' table.
-- The lifespan is defined as the number of years the band was active.

SELECT 
    band_name,  -- Select the name of the band
    CASE 
        WHEN split IS NULL THEN 2022 - formed  -- If the band has not split, calculate the lifespan as the current year (2022) minus the year the band was formed
        ELSE split - formed  -- If the band has split, calculate the lifespan as the year they split minus the year they were formed
    END AS lifespan  -- Alias the calculated lifespan as 'lifespan'
FROM 
    metal_bands;  -- From the 'metal_bands' table
