-- ## VIEWS ##:

-- Write an SQL query that finds all the customer info and sorts it alphabetically by country save this query as a view
Use Chinook;
Drop View CustomerData;
Create View CustomerData
As
Select * 
From Customer
Order By Country;

Select * From CustomerData;

-- update the view to remove sensitive customer information, such as address, name etc. (update the view using REPLACE)
Create or Replace View CustomerData
As
Select customerid, Lastname, firstname, email
From Customer
Order By lastname;

Select * From CustomerData;



-- ## TABLE Constraints ##:

-- Use unique to alter our world data table to make sure one country cannot be inserted twice
Use CountryData;

Alter Table countries 
Add Constraint unique_country
Unique (country);

Describe countries;

-- Use check to alter our world data table to make sure a country has to have a population and landmass larger than 0 to be added to the table.
Alter Table countries
Modify Column population	int				Not Null	Check (population > 0),
Modify Column `Area (km^2)`	decimal(50,2)	Not Null	Check (`Area (km^2)` > 0);

Describe countries;

-- ## Additional SQL Practice ##: 

-- Sort data by the longest capital names.
Select *, length(capital) As Length_of_Capital_Name
From Countries
Order By Length_of_Capital_Name DESC;

-- Sort data by the shortest country names.
Select *, length(capital) As Length_of_Country_Name
From Countries
Order By Length_of_Country_Name;

-- find the total population of all two word countries
Select Country
From countries
Where instr(trim(country), ' ') > 0;

-- find the total population of all three word countries