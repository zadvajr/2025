-- BETWEEN Date Values
-- The BETWEEN operator can also be used on date values.

-- Example
-- Select all orders between 12. of April 2023 and 5. of May 2023:

SELECT * FROM orders
WHERE order_date BETWEEN '2023-04-12' AND '2023-05-05';