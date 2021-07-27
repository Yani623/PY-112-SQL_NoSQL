import sqlite3

work_dir = "/Users/yani/Desktop/PY-112-MySQL/"
db_name =  "world_populations.db"

# print(work_dir + db_name)
conn = sqlite3.connect(work_dir + db_name)
c = conn.cursor()

c.execute('''SELECT sum(migrants) 
FROM pop_data 
WHERE country in ("Canada", "France", "Germany", "Italy", "Japan", "United Kingdom", "Unites States")
and migrants > 0
''')

g7Migrants = int(str(c.fetchone())[1:-2])

# print(f'Total number of migrants from G7 nations = {g7Migrants}')


c.execute('''SELECT sum(migrants) 
FROM pop_data 
WHERE migrants > 0;
''')
totalMigrants = int(str(c.fetchone())[1:-2])
# print(totalMigrants)

g7_world_migrant_ratio = round(g7Migrants/totalMigrants * 100, 2)
print(f'G7 countries take in {g7_world_migrant_ratio}% of the migrants taken in by all countries')


# WHERE country in ("Canada", "France", "Germany", "Italy", "Japan", "United Kingdom", "Unites States")