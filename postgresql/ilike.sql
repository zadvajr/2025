-- ILIKE
-- Note: The LIKE operator is case sensitive, if you want to do a case insensitive search, use the ILIKE operator instead.

-- Example
-- Return all customers with a name that contains the letter 'A' or 'a':

SELECT * FROM customers
WHERE customer_name ILIKE '%A%';