-- This SQL script creates an index named 'idx_name_first' on the 'names' table.
-- The index is created on the first character of the 'name' column.
-- Indexing the first character can improve query performance for searches that filter by the initial character of the 'name' column.

CREATE INDEX idx_name_first
ON names(name(1));  -- Create an index on the first character of the 'name' column in the 'names' table
