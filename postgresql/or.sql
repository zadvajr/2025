-- OR
-- The logical OR operator is used when you can accept that only one of many conditions is true:

-- Example
-- Return all records where the brand is 'Volvo' OR the year is 1975:

SELECT * FROM cars
WHERE brand = 'Volvo' OR year = 1975;