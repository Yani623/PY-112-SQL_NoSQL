-- Given the dataset provided MOCK_DATA.csv, do the following:

-- load the csv using this command
-- LOAD DATA LOCAL INFILE '/home/myfile.csv'
-- INTO TABLE mock_data FIELDS TERMINATED BY ','
-- ENCLOSED BY '"' LINES TERMINATED BY '\n';

-- sort the IP addresses by the first three digits (network identifier)
SELECT ip_address from Mock_table order by cast(SUBSTRING_INDEX(ip_address, '.', 1) as signed);

-- What are all the domains in the emails (domain i.e. : @engadget.com)
Select Distinct(Substring((email) , Position( "@" In email) )) From Mock_Table;
-- Dakota's solution:
-- 	SELECT DISTINCT substring_index(email, '@', -1) AS Domains
-- 	FROM mock_table
-- 	GROUP BY Domains;

-- How many times each domain used sorted descending.
SELECT (SUBSTRING_INDEX(email, '@', -1)) AS domain
, count(ID) as totalCount
FROM mock_table
group by domain
order by totalCount desc;

-- Count each top domain and sort descending
Select SUBSTRING(email, LOCATE('.', email) + 0) AS 'domain', count('domain') as common 
from mock_table
group by domain order by common desc;

-- select SUBSTRING(email, LOCATE('.', email) + 0) AS domain, count(SUBSTRING(email, LOCATE('.', email) + 0)) as common from mock_Table group by domain order by common desc;