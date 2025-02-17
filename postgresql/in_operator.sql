-- IN
-- The IN operator allows you to specify a list of possible values in the WHERE clause.

-- The IN operator is a shorthand for multiple OR conditions.

-- Example
-- Return all customers from 'Germany', France' or 'UK':

SELECT * FROM customers
WHERE country IN ('Germany', 'France', 'UK');