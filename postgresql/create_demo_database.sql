-- Create Demo Database
-- Demo Database
-- Up until now in this tutorial we have worked with a very small and simple table in our PostgreSQL database.
-- Now we want to create more tables with more content to be able to demonstrate more database features.

-- We will create these 6 tables in our PostgreSQL database:
-- categories
-- customers
-- products
-- orders
-- order_details
-- testproducts

-- Below we have listed all the SQL statements you need to create those tables, with content.
-- You are not required to create the tables on your own system to continue with this tutorial,
-- but you might better understand how PostgreSQL and SQL statements work.

-- Make sure you are connected to the database.
-- If not, follow the steps in the SQL Shell chapter of this tutorial.

-- Once you are connected, you are ready to write SQL statements!

-- CATEGORIES
-- The following SQL statement will create a table named categories:
-- CREATE TABLE categories
CREATE TABLE categories (
    category_id SERIAL NOT NULL PRIMARY KEY,
    category_name VARCHAR(255),
    description VARCHAR(255)
);

-- Result: CREATE TABLE