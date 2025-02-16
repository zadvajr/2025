-- Set Column Name
-- When you use MIN() or MAX(), the returned column will be named min or max by default. To give the column a new name, use the AS keyword.

-- Example
-- Return the lowest price, and name the column lowest_price:

SELECT MIN(price) AS lowest_price
FROM products;