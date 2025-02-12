-- Text Fields vs. Numeric Fields
-- PostgreSQL requires quotes around text values.

-- However, numeric fields should not be enclosed in quotes:

-- Example
SELECT * FROM customers
WHERE customer_id = 19;

-- Quotes around numeric fields will not fail,
-- but it is good practice to always write numeric values without quotes.
