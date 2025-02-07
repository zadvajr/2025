-- Update Multiple Columns
-- To update more than one column separate the name/values pairs with a comma
-- Example: Update color and year for the Toyota

UPDATE cars
SET color = 'white', year = 1970
WHERE brand = 'Toyota';

-- Result: UPDATE 1 - Which means 1 record was affected by the UPDATE statement