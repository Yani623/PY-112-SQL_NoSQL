import requests # Requests is an HTTP library that allows you to send HTTP/1.1 requests extremely easily. 
from bs4 import BeautifulSoup 

url = 'https://www.scrapethissite.com/pages/simple' 
result = requests.get(url)
soup = BeautifulSoup(result.content, 'html.parser')

all_countries = soup.find_all("div", {"class": "col-md-4 country"})
# print(all_countries[0].prettify())


country_data = []
for entry in all_countries:
    country = entry.find('h3').get_text().strip()
    capital = entry.find('span', {"class": "country-capital"}).get_text()
    population = int(entry.find('span', class_= "country-population").get_text())
    # print(population)
    area = int(round(float((entry.find("span", class_ = "country-area").get_text()))))
    # print(area)
    if population <= 0 or area <= 0:
        population_density = 0
    else:
        population_density = population/int(round(area))
    country_data.append((country, capital, population, area, population_density))


print(country_data[0])


import mysql.connector
from dotenv import dotenv_values

config = dotenv_values(".env")  

mydb = mysql.connector.connect(
host=config['HOST'],
user=config['USER'],
password=config['PASSWORD'],
database=config['DATABASE'])

mycursor = mydb.cursor()

mycursor.execute('Create Database If Not Exists CountryData;')
mycursor.execute('Use CountryData;')

mycursor.execute('Drop Table If Exists Countries;')
mycursor.execute('''Create Table If Not Exists Countries
(
id                  int             Not Null  Auto_Increment  Primary Key,
Country             varchar(250)    Not Null,
Capital             carchar(250)    Not Null,
Population          int             Not Null,
Area (km^2)         decimal(50, 2)  Not Null,
Population_Density  decimal(50,2)   Not Null;
''')

mycursor.executemany('''Insert Into Table Countries (id, country, capital, population, area, population_density) Values (%s, %s, %s, %s, %s, %s)''', country_data)


mydb.commit()
# mycursor.executemany('Select * From "list_name"')
# for x in mycursor:
#   print(x)
mydb.close()