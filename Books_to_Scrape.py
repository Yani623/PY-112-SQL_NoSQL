''' Extract all information you can about each book from http://books.toscrape.com/ '''

import requests
from bs4 import BeautifulSoup
from pprint import pprint
from word2number import w2n

url = 'http://books.toscrape.com/'
result = requests.get(url)
soup = BeautifulSoup(result.content, 'html.parser')
# print(soup.prettify())


ol_tag = soup.find('ol')
li_tags = ol_tag.find_all('li') #list that contains all the info we need (Title, rating, price...) for each book.
# print(li_tags[0].prettify())


''' Create loop for retrieving data for each book'''

dataLi = []
for li in li_tags:

    title = str(li.find('h3').find('a').get('title'))

    description_link = url + li.find('div', {"class": "image_container"}).find('a').get('href')

    star_rating = w2n.word_to_num((li.find_all('p')[0].get('class'))[-1])

    price = float(li.find('p', {"class": "price_color"}).get_text()[1:])

    in_stock = li.find('p', {"class": "instock availability"}).get_text().strip().lower()
    if in_stock == "in stock":
        in_stock = 'Y'
    else:
        in_stock = 'N' 

    dataLi.append((title, description_link, star_rating, price, in_stock))
# pprint(dataLi)



'''Creating and Modifying Database'''

import mysql.connector
from dotenv import dotenv_values

config = dotenv_values(".env")  

mydb = mysql.connector.connect(
host=config['HOST'],
user=config['USER'],
password=config['PASSWORD'],
database=config['DATABASE'])

mycursor = mydb.cursor()

# mycursor.execute('Drop Database If Exists BookstoScrape;')
mycursor.execute('Create Database If Not Exists BookstoScrape;')

mycursor.execute('Use BookstoScrape;')

mycursor.execute('Drop Table If Exists Books;')

mycursor.execute('''Create Table If Not Exists Books
(
id                  int             Not Null   AUTO_INCREMENT   Primary Key,
title               varchar(250)    Not Null,
description_link    varchar(2083)    Not Null,
star_rating         int             Not Null,
`price(£)`          decimal(5 , 2)   Not Null,
in_stock            varchar(1)  Not Null
);''')

mycursor.executemany('''INSERT Into Books (title, description_link, star_rating, `price(£)`, in_stock) VALUES (%s, %s, %s, %s, %s)''', dataLi)




mydb.commit()
# mycursor.executemany('Select * From "list_name"')
# for x in mycursor:
#   print(x)
mydb.close()



