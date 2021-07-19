SELECT * FROM CountryData.Countries;

Use CountryData;
-- Which country has the largest population ( using sql)
Select *
From Countries
Order By population DESC
Limit 1;

-- Which country has the longest name (using sql)
SELECT 
    Country, LENGTH(country) AS NameLength
FROM
    Countries
GROUP BY country
ORDER BY NameLength DESC
LIMIT 1;

-- Which countries have a population between 30,000 and 500,000? (using sql)
Select Country, Population
From Countries
Where Population Between 30000 and 500000
Order By Population DESC;


-- Which countries have a population greater than 500,000 and start with the letter A? (using sql)
Select Country, Population
From Countries
Where Population > 500000 And INSTR(country, 'a') = 1
Order By Population DESC;
