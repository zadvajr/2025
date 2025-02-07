-- The DELETE statement
-- The DELETE statement is used to delete existing records in a table
-- Note: Be careful when deleting records in a table! Notice the WHERE clause in the DELETE statement.
-- The WHERE clause specifies which record(s) should be deleted.
-- If you omit the WHERE clause,
-- all records in the table will be deleted!.
-- To delete the record(s) where brand is 'Volvo', use this statement:

-- Example
-- Delete all records where brand is 'Volvo':
DELETE FROM cars
WHERE brand = 'Volvo';

-- Result: DELETE 1 - which means 1 record is deleted
