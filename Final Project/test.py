'''Cleaning Data and importing into cust_accounts'''
import csv
import os
import string
import pprint

os.chdir(r'/Users/yani/Desktop/PY-112-MySQL/Final Project')

import mysql.connector
from dotenv import dotenv_values

config = dotenv_values(".env")  

mydb = mysql.connector.connect(
  host=config['HOST'],
  user=config['USER'],
  password=config['PASSWORD'],

  database=config['DATABASE'])

mycursor = mydb.cursor()
# 'cust_accounts': acct_num, trade_type (will come from the cust_transactions table), gender, last_name, first_name, salary, city, state

with open('cust_accounts.csv', newline = '') as cust_accounts:
    data1 = csv.DictReader(cust_accounts)
    
    # Get string of symbols from ascii characters:
    symbols = string.printable[(string.printable.index('!')):].replace('-','')
    for row in data1:
        row.pop('') #Removes the dict key, value pair for the random keyname = None.  
        # Removes symbols (except '-') found in any of the dict values:
        for x,y in row.items():
            for i in y:
                if i in symbols:
                    # print(row)
                    row[x] = str(y).replace(i, ' ')
        row['acct_num'] = row['acct_num'].strip().upper()
        # print(row['acct_num'])
        row['gender'] = str(row['gender'].strip())
        row['last_name'] = row['last_name'].strip().capitalize()
        row['first_name'] = row['first_name'].strip().capitalize()
        row['salary'] = row['salary'].replace("$", "").strip()
        row['city'] = row['city'].strip().title()
        row['state'] = row['state'].strip().upper()

        # Could not insert data using executemany.
        cust_accounts_tuple = (row['acct_num'], row['gender'], row['last_name'], row['first_name'], row['salary'], row['city'], row['state'])
        query = f'''Insert Into cust_accounts (acct_num,gender,last_name,first_name,salary,city,state) Values {cust_accounts_tuple}'''
        # print(query)

        mycursor.execute(query)
        
mydb.commit()

# mycursor.execute('''Select * From cust_accounts Limit 15;''')
# for x in mycursor:
#     print(x)

mydb.close()
