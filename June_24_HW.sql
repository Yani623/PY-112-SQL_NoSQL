-- 1: Provide a query showing Customers (just their full names, customer ID and country) who are not in the US.
Select CONCAT(LastName, ',', FirstName) As 'Full Name',CustomerID,Country
From Customer
Where Country <>"USA";

-- 2: Provide a query only showing the Customers from Brazil.
Select FirstName,LastName,CustomerID,Country
From Customer
Where Country = "Brazil";

-- 3: Provide a query showing the Invoices of customers who are from Brazil. The resultant table should show the customer's full name,Invoice ID, Date of the invoice and billing country.
Select a.FirstName, a.LastName, b.InvoiceID, b.InvoiceDate, b.BillingCountry
From Customer AS a
Inner Join Invoice AS b
ON a.CustomerID = b.CustomerID
Where Country = "Brazil";

-- 4: Provide a query showing only the Employees who are Sales Agents.
Select *
From Employee
Where Title = 'Sales Support Agent';

-- 5: Provide a query showing a unique list of billing countries from the Invoice table.
Select Distinct BillingCountry
From Invoice
Order By BillingCountry; -- This puts it in alphabetical order

-- 6: Provide a query showing the invoices of customers who are from Brazil.
Select *
From Invoice
Where BillingCountry = "Brazil";

-- 7: Provide a query that shows the invoices associated with each sales agent. The resultant table should include the Sales Agent's full name.
Select e.LastName, e.FirstName, i.InvoiceID
From Customer As c
Join Invoice As i
On c.CustomerID = i.CustomerID
Join Employee As e
On c.SupportRepID = e.EmployeeID;

-- 8: Provide a query that shows the Invoice Total, Customer name, Country and Sale Agent name for all invoices and customers.
Select c.LastName, c.FirstName, c.Country, e.LastName, e.FirstName, i.Total
From Customer as c
Inner Join Invoice As i
On c.CustomerId = i.CustomerId
Inner Join Employee As e
On c.SupportRepId = e.EmployeeId;

-- 9: How many Invoices were there in 2009 and 2011? What are the respective total sales for each of those years?
Select InvoiceID, Total, Date
From Invoice
Where InvoiceDate Like "2011%"  ;


-- 10: Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for Invoice ID 37.
Select Count(*)
From InvoiceLine
Where InvoiceID = '37';

select * From InvoiceLine;
-- 11: Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for each Invoice. HINT: GROUP BY
Select InvoiceId, Count(*) As 'Line Items'
From InvoiceLine
Group By InvoiceID;

-- 12: Provide a query that includes the track name with each invoice line item.
Select i.InvoiceLineID, t.Name
From Track as t
Inner Join InvoiceLine as i
On t.TrackID = i.TrackID
Order By InvoiceLineId;

-- 13: Provide a query that includes the purchased track name AND artist name with each invoice line item.
Select i.InvoiceLineID, t.Name, t.Composer
From InvoiceLine as i
Inner Join Track as t
On i.TrackId = t.TrackId
Order By InvoiceLineID;

-- 14: Provide a query that shows the # of invoices per country. HINT: GROUP BY
Select Count(InvoiceID) As '# of Invoices', BillingCountry
From Invoice
Group By BillingCountry;
Select * From Invoice Limit 2;


-- 15: Provide a query that shows the total number of tracks in each playlist. The Playlist name should be include on the resultant table.
Select pl.PlaylistId, p.Name, count(pl.TrackID) As '# of Tracks' 
From Playlist As p
Inner Join PlaylistTrack as pl
On p.PlaylistId = pl.PlaylistId
Group By PlaylistId;


-- 16: Provide a query that shows all the Tracks, but displays no IDs. The resultant table should include the Album name, Media type and Genre.
Select t.Name As 'Track Name', m.Name As 'Media Type', g.Name As 'Genre'
From Track As t
Inner Join MediaType as m
On t.MediaTypeId = m.MediaTypeId
Inner Join Genre As g
On t.GenreId = g.GenreId;


-- 17: Provide a query that shows all Invoices but includes the # of invoice line items.
Select i.*, Count(il.InvoiceID) As '# of Line Items'
From Invoice as i
Inner Join InvoiceLine As il
On i.InvoiceID = il.InvoiceId
Group By InvoiceID;


-- 18) Provide a query that shows total sales made by each sales agent.
Select Concat(e.LastName,',', e.FirstName) As 'Employee Name', sum(i.total) As 'Total Sales'
From invoice i
Inner Join Customer c
On c.CustomerID = i.CustomerId
Inner Join Employee e
On c.SupportRepId = e.EmployeeId
Group by EmployeeID;

-- 19) Which sales agent made the most in sales in 2009?
Select Concat(e.LastName,',', e.FirstName) As 'Employee Name', sum(i.total) As 'Total Sales'
From invoice i
Inner Join Customer c
On c.CustomerID = i.CustomerId
Inner Join Employee e
On c.SupportRepId = e.EmployeeId
Where i.InvoiceDate Like "2009%"
Group By EmployeeID
Order By 'Total Sales'
Limit 1;


-- 20) Which sales agent made the most in sales in 2010?
Select Concat(e.LastName,',', e.FirstName) As 'Employee Name', sum(i.total) As 'Total Sales'
From invoice i
Inner Join Customer c
On c.CustomerID = i.CustomerId
Inner Join Employee e
On c.SupportRepId = e.EmployeeId
Where i.InvoiceDate Like "2010%"
Group By EmployeeID
Order By 'Total Sales'
Limit 1;


-- 21) Which sales agent made the most in sales over all?
Select Concat(e.LastName,',', e.FirstName) As 'Employee Name'
From invoice i
Inner Join Customer c
On c.CustomerID = i.CustomerId
Inner Join Employee e
On c.SupportRepId = e.EmployeeId
Group by EmployeeID
Order By sum(i.total)
Limit 1;


-- 22) Provide a query that shows the # of customers assigned to each sales agent.
Select Concat(e.LastName,',', e.FirstName) As 'Employee Name', Count(c.CustomerId) As '# of Customers' 
From Employee e
Inner Join Customer c
On e.EmployeeId = c.SupportRepId
Group By EmployeeId;


-- 23) Provide a query that shows the total sales per country. Which country's customers spent the most?
Select BillingCountry, sum(Total) As 'Total Sales'
From Invoice
Group By BillingCountry
Order By sum(Total) DESC
Limit 1;


-- 24) Provide a query that shows the most purchased track of 2013.
Select t.Name As 'Track Name', Count(il.InvoiceId) As '# Purchased'
From Track t
Inner Join InvoiceLine il
On il.TrackId = t.TrackId
Inner Join Invoice i
On il.invoiceId = i.invoiceId
Where i.InvoiceDate Like '2013%'
Group By Name
Order By Count(il.InvoiceId) DESC
Limit 1;

-- 25) Provide a query that shows the top 5 most purchased tracks over all.
Select t.Name As 'Track Name', Count(il.InvoiceId) As '# Purchased'
From Track t
Inner Join InvoiceLine il
On il.TrackId = t.TrackId
Inner Join Invoice i
On il.invoiceId = i.invoiceId
Group By Name
Order By Count(il.InvoiceId) DESC
Limit 5;


-- 26) Provide a query that shows the top 3 best selling artists.
Select t.composer As 'Artist', count(il.InvoiceID) As "# Tracks Sold"
From Track t
Inner Join InvoiceLine il
On t.TrackId = il.TrackId
Group By Composer
Order by '# Tracks Sold' DESC;


-- 27) Provide a query that shows the most purchased Media Type.
Select m.Name As 'MediaType', count(il.InvoiceID) As "# Purchased"
From Track t
Inner Join InvoiceLine il
On t.TrackId = il.TrackId
Inner Join MediaType m
On t.MediaTypeId = m.MediaTypeId
Group By m.Name
Order by count(il.InvoiceID) DESC
Limit 1;


-- 1) Find the employee that has been employed the longest and show all employees by postal code.
Select Concat(LastName, ',', FirstName) As 'Employee Name', HireDate
From Employee
Order By HireDate
Limit 1;

-- 2) Find the state with the most and least amount of employees.



-- 3) Find how long each playlist is in milliseconds and show ranking (order by)
Select p.Name As 'Playlist', Sum(t.Milliseconds) As 'Length (msec)'
From Track t
Inner Join PlaylistTrack pt
On t.TrackId = pt.TrackId
Inner Join Playlist p
On p.PlaylistId = pt.PlaylistId
Group By p.name
Order By sum(t.Milliseconds);







