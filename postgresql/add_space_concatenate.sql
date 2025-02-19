-- Note: In the result of the example above we are missing a space between product_name
-- and unit. To add a space when concatenating, use || ' ' ||.

-- Example
-- Concatenate, with space:

SELECT product_name || ' ' || unit AS product
FROM products;
