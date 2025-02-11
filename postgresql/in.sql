-- IN
-- The IN operator is used when a column's value matches any of the values in a list:

-- Example
-- Return all records where the brand is present in this list: ('Volvo', 'Mercedes', 'Ford'):

SELECT * FROM cars
WHERE brand IN ('Volvo', 'Mercedes', 'Ford');