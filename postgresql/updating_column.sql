-- The UPDATE statement
-- The UPDATE statement is used to modify values in existing record in a table

-- Example
-- Set the color of Volvo to red
UPDATE cars
SET color = 'red'
WHERE brand = 'Volvo';

-- Result will be: UPDATE 1
-- Which means that 1 row was affected by the UPDATE statement
-- Be careful when updating records. If you omit the WHERE clause, ALL records will be updated!