'''
Links: 
https://docs.python.org/3/library/csv.html (how to read csv in python)


Write a pure python program that does the following from the CSV file. 

1) read the csv file dogs_data.csv 
2) generate INSERT INTO statements with the data  as a string

input -> csv file


output-> 

INSERT INTO cats ( name, owner, birth) VALUES
    ( 'Sandy', 'Lennon', '2015-01-03' ),
    ( 'Cookie', 'Casey', '2013-11-13' ),
    ( 'Charlie', 'River', '2016-05-21' );
'''

# open("dog_data.csv", "r")


# import csv
# with open('dog_data.csv', newline='') as csvfile:
#     rows = []
#     # rows2 = [rows.sep="\n"]
#     spamreader = csv.reader(csvfile, delimiter=' ') #returns a list of strings
    
#     for row in spamreader:
#         # print(', '.join(row))
#         str(row)
#         rows.append((tuple(row)))

# print("INSERT INTO cats (name, owner, birth, type) VALUES" )
# print( *rows,sep='\n')


'''Join method:
used on lists to join elements into a string. 

'''
import csv
import sqlite3

with open('inventory.csv', newline='') as fin:
    # print(fin.read()) #prints out the inventory list that we just opened and called fin.

    dr = csv.DictReader(fin) #returns a list of dictionaries.
    inventory = []
    for row in dr:
        inventory.append(tuple(row.values()))

# print(inventory)

for x in range(len(inventory)):
    inventory[x] = list(inventory[x])
    
    inventory[x][-1] = str(round(int(inventory[x][-2]) * float(inventory[x][-3]), 3))

    inventory[x] = tuple(inventory[x])
    
    
    # x[-1] = int(x[-2]) * float(x[-3])


# price_extended = (int(inventory[x,-2]) * float(inventory[x,-3])) for x inventory[x,-1] in inventory

# price_extended()
print(inventory)

# import csv, sqlite3
# from pprint import pprint
# def main_solution():
# 	with open('../sql-data/inventory.csv','r') as fin:
# 		dr = csv.DictReader(fin)
# 		all_vals = []
# 		for entry in dr:
# 			csv_vals = list(entry.values())[:-1]
# 			price_quantity = round(float(entry['price']) * int(entry['quantity']), 2)
# 			csv_vals.append(price_quantity)
# 			all_vals.append(tuple(csv_vals))
# 		print(all_vals)
# 	#create database, add new table, drop table if already there.	
# 	con = sqlite3.connect("hardware_store.db") # change to 'sqlite:///your_filename.db'
# 	cur = con.cursor()
# 	cur.execute("""DROP TABLE inventory""")
# 	cur.execute("""CREATE TABLE IF NOT EXISTS inventory (
# 	    item_id TEXT,
# 	    item TEXT,
# 	    price REAL,
# 	    quantity INTEGER,
# 	   	price_extended REAL)
# 	""")
# 	cur.executemany("""INSERT INTO inventory VALUES (?,?,?,?,?)""", all_vals )
# 	cur.execute("""SELECT * from inventory""")
# 	data = cur.fetchall()
# 	pprint(data) 
# if __name__ == '__main__':
# 	main_solution()