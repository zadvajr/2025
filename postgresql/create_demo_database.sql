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

-- The following statement will fill the categories table with content
INSERT INTO categories (category_name, description)
VALUES
  ('Beverages', 'Soft drinks, coffees, teas, beers, and ales'),
  ('Condiments', 'Sweet and savory sauces, relishes, spreads, and seasonings'),
  ('Confections', 'Desserts, candies, and sweet breads'),
  ('Dairy Products', 'Cheeses'),
  ('Grains/Cereals', 'Breads, crackers, pasta, and cereal'),
  ('Meat/Poultry', 'Prepared meats'),
  ('Produce', 'Dried fruit and bean curd'),
  ('Seafood', 'Seaweed and fish');

-- Result: INSERT 0 8

-- CUSTOMERS
-- The following SQL statement will create a table named customers:
-- CREATE TABLE customers
CREATE TABLE customers (
  customer_id SERIAL NOT NULL PRIMARY KEY,
  customer_name VARCHAR(255),
  contact_name VARCHAR(255),
  address VARCHAR(255),
  city VARCHAR(255),
  postal_code VARCHAR(255),
  country VARCHAR(255)
);

-- Result: CREATE TABLE

-- The following SQL statement will fill the customers table with content:

-- INSERT INTO customers
INSERT INTO customers (customer_name, contact_name, address, city, postal_code, country)
VALUES
  ('Alfreds Futterkiste', 'Maria Anders', 'Obere Str. 57', 'Berlin', '12209', 'Germany'),
  ('Ana Trujillo Emparedados y helados', 'Ana Trujillo', 'Avda. de la Constitucion 2222', 'Mexico D.F.', '05021', 'Mexico'),
  ('Antonio Moreno Taquera', 'Antonio Moreno', 'Mataderos 2312', 'Mexico D.F.', '05023', 'Mexico'),
  ('Around the Horn', 'Thomas Hardy', '120 Hanover Sq.', 'London', 'WA1 1DP', 'UK'),
  ('Berglunds snabbkoep', 'Christina Berglund', 'Berguvsvegen 8', 'Lulea', 'S-958 22', 'Sweden'),
  ('Blauer See Delikatessen', 'Hanna Moos', 'Forsterstr. 57', 'Mannheim', '68306', 'Germany'),
  ('Blondel pere et fils', 'Frederique Citeaux', '24, place Kleber', 'Strasbourg', '67000', 'France'),
  ('Bolido Comidas preparadas', 'Martin Sommer', 'C/ Araquil, 67', 'Madrid', '28023', 'Spain'),
  ('Bon app', 'Laurence Lebihans', '12, rue des Bouchers', 'Marseille', '13008', 'France'),
  ('Bottom-Dollar Marketse', 'Elizabeth Lincoln', '23 Tsawassen Blvd.', 'Tsawassen', 'T2F 8M4', 'Canada'),
  ('Bs Beverages', 'Victoria Ashworth', 'Fauntleroy Circus', 'London', 'EC2 5NT', 'UK'),
  ('Cactus Comidas para llevar', 'Patricio Simpson', 'Cerrito 333', 'Buenos Aires', '1010', 'Argentina'),
  ('Centro comercial Moctezuma', 'Francisco Chang', 'Sierras de Granada 9993', 'Mexico D.F.', '05022', 'Mexico'),
  ('Chop-suey Chinese', 'Yang Wang', 'Hauptstr. 29', 'Bern', '3012', 'Switzerland'),
  ('Comercio Mineiro', 'Pedro Afonso', 'Av. dos Lusiadas, 23', 'Sao Paulo', '05432-043', 'Brazil'),
  ('Consolidated Holdings', 'Elizabeth Brown', 'Berkeley Gardens 12 Brewery ', 'London', 'WX1 6LT', 'UK'),
  ('Drachenblut Delikatessend', 'Sven Ottlieb', 'Walserweg 21', 'Aachen', '52066', 'Germany'),
  ('Du monde entier', 'Janine Labrune', '67, rue des Cinquante Otages', 'Nantes', '44000', 'France'),
  ('Eastern Connection', 'Ann Devon', '35 King George', 'London', 'WX3 6FW', 'UK'),
  ('Ernst Handel', 'Roland Mendel', 'Kirchgasse 6', 'Graz', '8010', 'Austria'),
  ('Familia Arquibaldo', 'Aria Cruz', 'Rua Oros, 92', 'Sao Paulo', '05442-030', 'Brazil'),
  ('FISSA Fabrica Inter. Salchichas S.A.', 'Diego Roel', 'C/ Moralzarzal, 86', 'Madrid', '28034', 'Spain'),
  ('Folies gourmandes', 'Martine Rance', '184, chaussee de Tournai', 'Lille', '59000', 'France'),
  ('Folk och fe HB', 'Maria Larsson', 'Akergatan 24', 'Brecke', 'S-844 67', 'Sweden'),
  ('Frankenversand', 'Peter Franken', 'Berliner Platz 43', 'Munchen', '80805', 'Germany'),
  ('France restauration', 'Carine Schmitt', '54, rue Royale', 'Nantes', '44000', 'France'),
  ('Franchi S.p.A.', 'Paolo Accorti', 'Via Monte Bianco 34', 'Torino', '10100', 'Italy'),
  ('Furia Bacalhau e Frutos do Mar', 'Lino Rodriguez ', 'Jardim das rosas n. 32', 'Lisboa', '1675', 'Portugal'),
  ('Galeria del gastronomo', 'Eduardo Saavedra', 'Rambla de Cataluna, 23', 'Barcelona', '08022', 'Spain'),
  ('Godos Cocina Tipica', 'Jose Pedro Freyre', 'C/ Romero, 33', 'Sevilla', '41101', 'Spain'),
  ('Gourmet Lanchonetes', 'Andre Fonseca', 'Av. Brasil, 442', 'Campinas', '04876-786', 'Brazil'),
  ('Great Lakes Food Market', 'Howard Snyder', '2732 Baker Blvd.', 'Eugene', '97403', 'USA'),
  ('GROSELLA-Restaurante', 'Manuel Pereira', '5th Ave. Los Palos Grandes', 'Caracas', '1081', 'Venezuela'),
  ('Hanari Carnes', 'Mario Pontes', 'Rua do Paco, 67', 'Rio de Janeiro', '05454-876', 'Brazil'),
  ('HILARION-Abastos', 'Carlos Hernandez', 'Carrera 22 con Ave. Carlos Soublette #8-35', 'San Cristobal', '5022', 'Venezuela'),
  ('Hungry Coyote Import Store', 'Yoshi Latimer', 'City Center Plaza 516 Main St.', 'Elgin', '97827', 'USA'),
  ('Hungry Owl All-Night Grocers', 'Patricia McKenna', '8 Johnstown Road', 'Cork', '', 'Ireland'),
  ('Island Trading', 'Helen Bennett', 'Garden House Crowther Way', 'Cowes', 'PO31 7PJ', 'UK'),
  ('Koniglich Essen', 'Philip Cramer', 'Maubelstr. 90', 'Brandenburg', '14776', 'Germany'),
  ('La corne d abondance', 'Daniel Tonini', '67, avenue de l Europe', 'Versailles', '78000', 'France'),
  ('La maison d Asie', 'Annette Roulet', '1 rue Alsace-Lorraine', 'Toulouse', '31000', 'France'),
  ('Laughing Bacchus Wine Cellars', 'Yoshi Tannamuri', '1900 Oak St.', 'Vancouver', 'V3F 2K1', 'Canada'),
  ('Lazy K Kountry Store', 'John Steel', '12 Orchestra Terrace', 'Walla Walla', '99362', 'USA'),
  ('Lehmanns Marktstand', 'Renate Messner', 'Magazinweg 7', 'Frankfurt a.M. ', '60528', 'Germany'),
  ('Lets Stop N Shop', 'Jaime Yorres', '87 Polk St. Suite 5', 'San Francisco', '94117', 'USA'),
  ('LILA-Supermercado', 'Carlos Gonzalez', 'Carrera 52 con Ave. Bolivar #65-98 Llano Largo', 'Barquisimeto', '3508', 'Venezuela'),
  ('LINO-Delicateses', 'Felipe Izquierdo', 'Ave. 5 de Mayo Porlamar', 'I. de Margarita', '4980', 'Venezuela'),
  ('Lonesome Pine Restaurant', 'Fran Wilson', '89 Chiaroscuro Rd.', 'Portland', '97219', 'USA'),
  ('Magazzini Alimentari Riuniti', 'Giovanni Rovelli', 'Via Ludovico il Moro 22', 'Bergamo', '24100', 'Italy'),
  ('Maison Dewey', 'Catherine Dewey', 'Rue Joseph-Bens 532', 'Bruxelles', 'B-1180', 'Belgium'),
  ('Mere Paillarde', 'Jean Fresniere', '43 rue St. Laurent', 'Montreal', 'H1J 1C3', 'Canada'),
  ('Morgenstern Gesundkost', 'Alexander Feuer', 'Heerstr. 22', 'Leipzig', '04179', 'Germany'),
  ('North/South', 'Simon Crowther', 'South House 300 Queensbridge', 'London', 'SW7 1RZ', 'UK'),
  ('Oceano Atlantico Ltda.', 'Yvonne Moncada', 'Ing. Gustavo Moncada 8585 Piso 20-A', 'Buenos Aires', '1010', 'Argentina'),
  ('Old World Delicatessen', 'Rene Phillips', '2743 Bering St.', 'Anchorage', '99508', 'USA'),
  ('Ottilies Keseladen', 'Henriette Pfalzheim', 'Mehrheimerstr. 369', 'Koln', '50739', 'Germany'),
  ('Paris specialites', 'Marie Bertrand', '265, boulevard Charonne', 'Paris', '75012', 'France'),
  ('Pericles Comidas clasicas', 'Guillermo Fernandez', 'Calle Dr. Jorge Cash 321', 'Mexico D.F.', '05033', 'Mexico'),
  ('Piccolo und mehr', 'Georg Pipps', 'Geislweg 14', 'Salzburg', '5020', 'Austria'),
  ('Princesa Isabel Vinhoss', 'Isabel de Castro', 'Estrada da saude n. 58', 'Lisboa', '1756', 'Portugal'),
  ('Que Delicia', 'Bernardo Batista', 'Rua da Panificadora, 12', 'Rio de Janeiro', '02389-673', 'Brazil'),
  ('Queen Cozinha', 'Lucia Carvalho', 'Alameda dos Canarios, 891', 'Sao Paulo', '05487-020', 'Brazil'),
  ('QUICK-Stop', 'Horst Kloss', 'Taucherstrasse 10', 'Cunewalde', '01307', 'Germany'),
  ('Rancho grande', 'Sergio Gutiarrez', 'Av. del Libertador 900', 'Buenos Aires', '1010', 'Argentina'),
  ('Rattlesnake Canyon Grocery', 'Paula Wilson', '2817 Milton Dr.', 'Albuquerque', '87110', 'USA'),
  ('Reggiani Caseifici', 'Maurizio Moroni', 'Strada Provinciale 124', 'Reggio Emilia', '42100', 'Italy'),
  ('Ricardo Adocicados', 'Janete Limeira', 'Av. Copacabana, 267', 'Rio de Janeiro', '02389-890', 'Brazil'),
  ('Richter Supermarkt', 'Michael Holz', 'Grenzacherweg 237', 'Genève', '1203', 'Switzerland'),
  ('Romero y tomillo', 'Alejandra Camino', 'Gran Via, 1', 'Madrid', '28001', 'Spain'),
  ('Santa Gourmet', 'Jonas Bergulfsen', 'Erling Skakkes gate 78', 'Stavern', '4110', 'Norway'),
  ('Save-a-lot Markets', 'Jose Pavarotti', '187 Suffolk Ln.', 'Boise', '83720', 'USA'),
  ('Seven Seas Imports', 'Hari Kumar', '90 Wadhurst Rd.', 'London', 'OX15 4NB', 'UK'),
  ('Simons bistro', 'Jytte Petersen', 'Vinbeltet 34', 'Kobenhavn', '1734', 'Denmark'),
  ('Specialites du monde', 'Dominique Perrier', '25, rue Lauriston', 'Paris', '75016', 'France'),
  ('Split Rail Beer & Ale', 'Art Braunschweiger', 'P.O. Box 555', 'Lander', '82520', 'USA'),
  ('Supremes delices', 'Pascale Cartrain', 'Boulevard Tirou, 255', 'Charleroi', 'B-6000', 'Belgium'),
  ('The Big Cheese', 'Liz Nixon', '89 Jefferson Way Suite 2', 'Portland', '97201', 'USA'),
  ('The Cracker Box', 'Liu Wong', '55 Grizzly Peak Rd.', 'Butte', '59801', 'USA'),
  ('Toms Spezialiteten', 'Karin Josephs', 'Luisenstr. 48', 'Manster', '44087', 'Germany'),
  ('Tortuga Restaurante', 'Miguel Angel Paolino', 'Avda. Azteca 123', 'Mexico D.F.', '05033', 'Mexico'),
  ('Tradicao Hipermercados', 'Anabela Domingues', 'Av. Ines de Castro, 414', 'Sao Paulo', '05634-030', 'Brazil'),
  ('Trails Head Gourmet Provisioners', 'Helvetius Nagy', '722 DaVinci Blvd.', 'Kirkland', '98034', 'USA'),
  ('Vaffeljernet', 'Palle Ibsen', 'Smagsloget 45', 'Arhus', '8200', 'Denmark'),
  ('Victuailles en stock', 'Mary Saveley', '2, rue du Commerce', 'Lyon', '69004', 'France'),
  ('Vins et alcools Chevalier', 'Paul Henriot', '59 rue de l Abbaye', 'Reims', '51100', 'France'),
  ('Die Wandernde Kuh', 'Rita Moller', 'Adenauerallee 900', 'Stuttgart', '70563', 'Germany'),
  ('Wartian Herkku', 'Pirkko Koskitalo', 'Torikatu 38', 'Oulu', '90110', 'Finland'),
  ('Wellington Importadora', 'Paula Parente', 'Rua do Mercado, 12', 'Resende', '08737-363', 'Brazil'),
  ('White Clover Markets', 'Karl Jablonski', '305 - 14th Ave. S. Suite 3B', 'Seattle', '98128', 'USA'),
  ('Wilman Kala', 'Matti Karttunen', 'Keskuskatu 45', 'Helsinki', '21240', 'Finland'),
  ('Wolski', 'Zbyszek', 'ul. Filtrowa 68', 'Walla', '01-012', 'Poland');

-- Result: INSERT 0 91
