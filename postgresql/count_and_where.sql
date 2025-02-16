-- COUNT and WHERE Clause

-- Example
-- Return the number of customers from London:

SELECT COUNT(customer_id)
FROM customers
WHERE city = 'London';
