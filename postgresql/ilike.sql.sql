-- ILIKE
-- Same as the LIKE operator, but ILIKE is case insensitive.

-- Example
-- Return all records where the model start with a 'm':

SELECT * FROM cars
WHERE model ILIKE 'm%';