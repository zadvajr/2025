-- The SELECT DISTINCT Statement
-- The SELECT DISTINCT statement is used to return only distinct (different) values.

-- Inside a table, a column often contains many duplicate values and sometimes you only want to list the different (distinct) values.

-- Example
-- Select only the DISTINCT values from the country column in the customers table:

SELECT DISTINCT country FROM customers;

-- Even though the customers table has 91 records,
-- it only has 21 different countries, and that is what you get as a result
-- when executing the SELECT DISTINCT statement above