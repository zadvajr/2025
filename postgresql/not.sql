-- NOT
-- The NOT operator can be used together with LIKE, ILIKE, IN, BETWEEN, and NULL operators to reverse the truth of the operator.

-- Example: NOT LIKE
-- Return all records where the brand does NOT start with a capital 'B' (case sensitive):

SELECT * FROM cars
WHERE brand NOT LIKE 'B%';

-- Example: NOT ILIKE
-- Return all records where the brand does NOT start with a 'b' (case insensitive):

SELECT * FROM cars
WHERE brand NOT ILIKE 'b%';

-- Example: NOT IN
-- Return all records where the brand is NOT present in this list: ('Volvo', 'Mercedes', 'Ford'):

SELECT * FROM cars
WHERE brand NOT IN ('Volvo', 'Mercedes', 'Ford');

-- Example: NOT BETWEEN
-- Return all records where the year is NOT between 1970 and 1980:

SELECT * FROM cars
WHERE year NOT BETWEEN 1970 AND 1980;

-- The NOT BETWEEN operator excludes the from and to values, meaning that in the above example, the result would not include cars made in 1970 and 1980.

-- Example: IS NOT NULL
-- Return all records where the model is NOT null:

SELECT * FROM cars
WHERE model IS NOT NULL;

-- The cars table has no columns with NULL values, so the example above will return all 4 rows.