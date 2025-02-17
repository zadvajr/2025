-- Contains
-- To return records that contains a specific letter or phrase, add the % both before and after the letter or phrase.

-- Example
-- Return all customers with a name that contains the letter 'A':

SELECT * FROM customers
WHERE customer_name LIKE '%A%';