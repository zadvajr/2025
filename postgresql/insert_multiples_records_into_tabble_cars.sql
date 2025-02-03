-- Insert Multiple Rows
-- To insert multiple rows of data, we use the same INSERT INTO statement, but with multiple values:

INSERT INTO cars (brand, model, year)
VALUES
  ('Volvo', 'p1800', 1968),
  ('BMW', 'M1', 1978),
  ('Toyota', 'Celica', 1975);
  
-- The SQL Shell application will return the following:

-- INSERT 0 3
-- Which means 3 rows were successfully inserted.

