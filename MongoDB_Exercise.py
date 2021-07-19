''' Import Data from Database CountryData and format into a dictionary for Mongodb ('''

import mysql.connector
from dotenv import dotenv_values

config = dotenv_values(".env")  

mydb = mysql.connector.connect(
host=config['HOST'],
user=config['USER'],
password=config['PASSWORD'],
database=config['DATABASE'])

mycursor = mydb.cursor()

mycursor.execute('Use CountryData;')
mycursor.execute('''Alter Table countries
Modify Column population_area	float(50,2)				Not Null	Check (population > 0),
Modify Column `Area (km^2)`	float(50,2)	Not Null	Check (`Area (km^2)` > 0);''')

column_names = []
mycursor.execute('''SELECT column_name 
FROM information_schema.columns 
WHERE table_name = 'Countries'
and column_name like '%%';''')
for x in mycursor:
    column_names.append(x)

column_names2 = []
# print(column_names)
## >>> [('id',), ('Country',), ('Capital',), ('population',), ('Area (km^2)',), ('Population_Density',)]

# mycursor.execute('''Select * From countries;''')
column_names2 = ['id', 'Country', 'Capital', 'Population', 'Area (km^2)', 'Population_Density']
country_DataLi = []
for x in mycursor:
    x_li = list(x)
    print(x_li)
    data_dict = dict(zip(column_names2, x_li))
    # for key, value in data_dict.items():
    #     value = value.replace('Decimal', '')
    country_DataLi.append(data_dict)
    
# print(country_DataLi[:2])

# Taro's Method:
mycursor.execute('''Select * From countries;''')
all_countries = mycursor.fetchall()
print(all_countries[1])







# mydb.commit()
mydb.close()