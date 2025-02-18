-- NOT IN
-- By using the NOT keyword in front of the IN operator, you return all records that are NOT any of the values in the list.

-- Example
-- Return all customers that are NOT from 'Germany', France' or 'UK':

SELECT * FROM customers
WHERE country NOT IN ('Germany', 'France', 'UK');