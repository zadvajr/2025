-- BETWEEN Text Values
-- The BETWEEN operator can also be used on text values.

-- The result returns all records that are alphabetically between the specified values.

-- Example
-- Select all products between 'Pavlova' and 'Tofu':

SELECT * FROM Products
WHERE product_name BETWEEN 'Pavlova' AND 'Tofu';