-- 1) Write a query to return the email, first name, last name, and Genre of all Rock Music listeners. Return your list ordered alphabetically by email address starting with A.

Select Distinct c.Email As 'Email', concat(c.LastName, ',', c.FirstName) As 'Name', g.Name As 'Genre'
From Genre g
Inner Join Track t
On g.GenreID = t.GenreID
Inner Join InvoiceLine il 
On t.TrackID = il.TrackID
Inner Join Invoice i 
On il.InvoiceID = i.InvoiceID
Inner Join Customer c 
On i.CustomerID = c.CustomerID
Where g.Name Like '%Rock%'
Order By c.email;


-- 2) Find which artist has earned the most according to the InvoiceLines?
Select a.name as 'Artist Name',
t.UnitPrice * Count(il.InvoiceId) as 'Total'
From InvoiceLine il
Inner Join Track t
On t.TrackId = il.TrackId
Inner Join Album as al
On t.AlbumId = al.AlbumId
Inner Join Artist As a
On al.ArtistID = a.ArtistID
Group By t.trackID
Order By Sum('Total');

-- Taros's Solution:
-- select a.Name
-- , sum(i.total)
-- from Invoice as i
-- join InvoiceLine as il
-- 	on i.InvoiceId = il.InvoiceId
-- join Track as t
-- 	on il.TrackId = t.TrackId
-- join Album as al
-- 	on t.AlbumId = al.AlbumId
-- join Artist as a
-- 	on al.ArtistId = a.ArtistId
-- group by a.Name
-- order by sum(i.total) desc
--  -- limit 1
-- ;


-- Dominic's Solution:
-- SELECT Y.NAME AS ARTIST_NAME, SUM(TOTAL) AS GRAND_TOTAL 
-- 	FROM 
-- 		(SELECT X.NAME, X.UNITPRICE * X.QUANTITY AS TOTAL
-- 				FROM
-- 					(SELECT AR.NAME, IL.UNITPRICE, IL.QUANTITY
-- 					FROM ARTIST AR
-- 					JOIN ALBUM AL ON AR.ARTISTID = AL.ARTISTID
-- 					JOIN TRACK T ON AL.ALBUMID = T.ALBUMID
-- 					JOIN INVOICELINE IL ON T.TRACKID = IL.TRACKID
-- 					ORDER BY 1 DESC) 
-- 		AS X) 
-- 	AS Y
-- GROUP BY 1
-- ORDER BY 2 DESC;

-- 3) Create two tables to model a shipping business. One table should be called orders and the other should be called shipments. The orders table should have an id, product name, amount. the shipping table should have a source country, destination country and product id as a foreign key. 

Create Database If Not Exists RandomCo;
Show Databases;
Use RandomCo;

Drop Table If Exists Orders;
Create Table If Not Exists orders
(
ProductID		INT				Not Null	Primary Key,
ProductName		Varchar(100)	Not Null,
Amount			Real			Not Null
);

Insert Into Orders (ProductID, ProductName, Amount) Values
('1','basketball', 5.00),
('2','soccer', 6.00),
('3','football', 9.00),
('4','cricket bat', 20.00);		

Drop Table if Exists shipments;
Create Table If Not Exists shipments
(
ProductID			INT				Not Null,
SourceCountry		Varchar(100)	Not Null,
DestinationCountry	Varchar(100)	Not Null,
Constraint fk_ProductID
Foreign Key (ProductID)
	References orders(ProductID)
		On Update Cascade
        On Delete Cascade
);

Insert Into shipments (ProductID,SourceCountry, DestinationCountry) Values
('1','india', 'usa'),
('2','vietnam', 'germany'),
('3','croatia', 'france'),
('4','france', 'usa');	




-- 2) update the prod id of product 2 so that it also updates in the child table 

Update orders
Set ProductID = 5
Where ProductID = 2;

Select * From Orders;
Select * From shipments;





