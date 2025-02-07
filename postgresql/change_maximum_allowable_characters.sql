-- Change Maximum Allowed Character
-- We also want to change the maximum number of characters allowed in the color column of the cars table

-- Example
-- Change the color column from VARCHAR(255) to VARCHAR(30):
ALTER TABLE cars
ALTER COLUMN year TYPE VARCHAR(30); -- Result: ALTER TABLE