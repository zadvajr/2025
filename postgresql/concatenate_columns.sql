-- Concatenate Columns
-- The AS keyword is often used when two or more fields are concatenated into one.

-- To concatenate two fields use ||.

-- Example
-- Concatenate two fields and call them product:

SELECT product_name || unit AS product
FROM products;