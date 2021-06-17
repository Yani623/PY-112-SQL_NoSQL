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


import csv
with open('dog_data.csv', newline='') as csvfile:
    rows = []
    # rows2 = [rows.sep="\n"]
    spamreader = csv.reader(csvfile, delimiter=' ')
    
    for row in spamreader:
        # print(', '.join(row))
        str(row)
        rows.append((tuple(row)))

print("INSERT INTO cats (name, owner, birth, type) VALUES" )
print( *rows,sep='\n')


'''Join method:
used on lists to join elements into a string. 

'''
list1 = 