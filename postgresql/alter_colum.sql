-- The ALTER statement
-- To change data type or size of a table column we have to use the ALTER TABLE STATEMENT
-- The ALTER TABLE statement is used to add, delete or modify columns in an existing table
-- The ALTER TABLE statement is also used to add and drop various constraints on an existing table

-- Alter Column
-- We want to change the type of the year column of the cars table from INT to VARCHAR(4)
-- To modify a column use the ALTER COLUMN statement and the TYPE keyword followed by the new data type:
-- Example: Change the year column from INT to VARCHAR

ALTER TABLE cars
ALTER COLUMN year TYPE VARCHAR(4);

-- Result: ALTER TABLE

-- Note: Some data types cannot be converted if the column has value.
-- E.g. numbers can always be converted to text, but text cannot always be converted to numbers.