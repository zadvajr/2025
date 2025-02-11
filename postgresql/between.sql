-- BETWEEN
-- The BETWEEN operator is used to check if a column's value is between a specified range of values:

-- Example
-- Return all records where the year is between 1970 and 1980:

SELECT * FROM cars
WHERE year BETWEEN 1970 AND 1980;

-- The BETWEEN operator includes the from and to values,
-- meaning that in the above example, the result would include cars made in 1970 and 1980 as well.