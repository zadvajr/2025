-- BETWEEN
-- The BETWEEN operator selects values within a given range. The values can be numbers, text, or dates.

-- The BETWEEN operator is inclusive: begin and end values are included.

-- Example
-- Select all products with a price between 10 and 15:

SELECT * FROM Products
WHERE Price BETWEEN 10 AND 15;