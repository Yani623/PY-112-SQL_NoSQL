import sqlite3
import csv
import pprint



'''Step 1. Create a db named Titanic.db'''

conn = sqlite3.connect("Titanic.db")

c = conn.cursor()



'''Step 2. create a table named passengers that has three fields (PassengerID TEXT, Name TEXT, Age TEXT)'''

# c.execute("""Create Table If Not Exists passengers (
#     PassengerID Text,
#     Name Text,
#     Age Text)
# """)

c.execute(''' Select avg)


# conn.commit()
# conn.close()

'''Step 3. Read data from titanic.csv ( passengerID, name, age ) and insert into passengers table you created'''
# Need to:
#   - Remove first row (labels)
#   - Extract ID: [0], Name: [3], Age: [5] into new list. 

# with open('Titanic.csv','r') as csv_file:
#     # print(csv_file.read())
#     dataPassenger = csv.reader(csv_file)    #each row read is returned as a list of strings. No datatype conversion is automatically performed. 
#     passengerData = []
#     tupleLi = []
#     for row in dataPassenger:
#         tupleLi = (row[0], row[3], row[5])
#         passengerData.append(tupleLi)


# print(passengers)

# c.executemany('''Insert Into passengers Values(?,?,?)''',passengerData)





'''Step 4: Find Moran, Mr. James and UPDATE his age to "50"'''


'''Step 5: Delete the row containing "Sjostedt, Mr. Ernst Adolf"'''


'''(Bonus) : Calculate the average age of all the passengers'''