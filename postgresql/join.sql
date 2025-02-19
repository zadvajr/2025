-- JOIN
-- A JOIN clause is used to combine rows from two or more tables, based on a related column between them.

Let's look at a selection from the products table:
-- Example
-- Join products to categories using the category_id column:

SELECT product_id, product_name, category_name
FROM products
INNER JOIN categories ON products.category_id = categories.category_id;