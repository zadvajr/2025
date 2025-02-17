The Undescore _ Wildcard
-- The _ wildcard represents a single character.

-- It can be any character or number, but each _ represents one, and only one, character.

-- Example
-- Return all customers from a city that starts with 'L' followed by one wildcard character, then 'nd' and then two wildcard characters:

SELECT * FROM customers
WHERE city LIKE 'L_nd__';