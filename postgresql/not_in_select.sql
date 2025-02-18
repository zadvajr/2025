-- NOT IN (SELECT)
-- The result in the example above returned 89 records, that means that there are 2 customers that haven't placed any orders.

-- Let us check if that is correct, by using the NOT IN operator.

-- Example
-- Return all customers that have NOT placed any orders in the orders table:

SELECT * FROM customers
WHERE customer_id NOT IN (SELECT customer_id FROM orders);