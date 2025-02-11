-- Not Equal To
-- The <> operator is used when you want to return all records where a column is NOT equal to a specified value:

-- Example
-- Return all records where the brand is NOT 'Volvo':

SELECT * FROM cars
WHERE brand <> 'Volvo';

-- You will get the same result with the != operator:

-- Example
-- Return all records where the brand is NOT 'Volvo':

SELECT * FROM cars
WHERE brand != 'Volvo';

-- The LIKE operator is case sensitive.