-- IN (SELECT)
-- You can also us a SELECT statement inside the parenthesis to return all records that are in the result of the SELECT statement.

-- Example
-- Return all customers that have an order in the orders table:

SELECT * FROM customers
WHERE customer_id IN (SELECT customer_id FROM orders);