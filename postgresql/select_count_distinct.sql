-- SELECT COUNT(DISTINCT)
-- We can also use the DISTINCT keyword in combination with the COUNT statement, which in the example below will return the number of different countries there are in the customers table.

-- Example
-- Return the number of different countries there are in the customers table:

SELECT COUNT(DISTINCT country) FROM customers;