-- With 2 Decimals
-- The above example returned the average price of all products, the result was 28.8663636363636364.
-- We can use the ::NUMERIC operator to round the average price to a number with 2 decimals:

-- Example
-- Return the average price of all the products, rounded to 2 decimals:

SELECT AVG(price)::NUMERIC(10,2)
FROM products;