-- Example
-- Join products to categories using the category_id column:

SELECT product_id, product_name, category_name
FROM products
INNER JOIN categories ON products.category_id = categories.category_id;