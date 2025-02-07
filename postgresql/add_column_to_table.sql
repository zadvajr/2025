-- Add Column
-- The ALTER Statement
-- To add column to an existing table, we have to use the ALTER TABLE statement
-- The ALTER TABLE statement is used to add, delete, or modify columns in an existing table
-- The ALTER TABLE statement is also used to add and drop various constraits on an existing table

-- Add Column
-- Assuming we want to add a column named "color" to our cars table,
-- When adding columns we must specify the data type of the column.
-- our color column will be a string, and we specify string types with the VARCHAR keyword
-- we also want to specify or restrict the number of characters to 255

-- Example
ALTER TABLE cars
ADD color VARCHAR(255);

-- Result: ALTER TABLE