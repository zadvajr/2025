-- If we add an ORDER BY clause to the example above, it will be a bit easier to read:

-- Example
-- Same example as above, but we sort it by product_name:

SELECT * FROM Products
WHERE product_name BETWEEN 'Pavlova' AND 'Tofu'
ORDER BY product_name;