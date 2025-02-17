-- LIKE
-- The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.

-- There are two wildcards often used in conjunction with the LIKE operator:

-- % The percent sign represents zero, one, or multiple characters
-- _ The underscore sign represents one, single character

-- Starts with
-- To return records that starts with a specific letter or phrase, add the % at the end of the letter or phrase.

-- Example
-- Return all customers with a name that starts with the letter 'A':

SELECT * FROM customers
WHERE customer_name LIKE 'A%';
