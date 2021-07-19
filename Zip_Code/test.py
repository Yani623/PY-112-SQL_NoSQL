

filePath = r'/Users/yani/Desktop/PY-112-MySQL/Zip_Code/zipcode_data.txt'

'''Using readlines()'''

# with open(filePath,'r') as zips:
#     ziplist = zips.readlines()   
#     print(ziplist)
#     zips.close()

    # Output: ['30004\n', 'Alpharetta, GA\n', '07652\n', 'Paramus, NJ\n', '90505\n',...
    # Need to get zip codes only and remove '\n'.


'''Using For Loop'''

zipList = []

with open(filePath,'r') as zips:
    for line in zips:
        # print(line)
        line = line.strip()
        if line.isnumeric():
            # line = (line,)
            zipList.append(line)

print(zipList[:5])







'''Get # of lines in txt file'''
# with open(filePath, 'r') as zips:
#     count = 0
#     for line in zips:
#         count += 1
# print(count)
# Count = 1000

'''Convert list of zips into dictionary using keys from other list'''
# keyLi = list(range(0,1001))
# zipList = []
# with open(filePath,'r') as zips:
#     for line in zips:
#         line = line.strip('\n')
#         if line.isnumeric():
#             # line = (line,)
#             zipList.append(line)

# zipDict = dict(zip(keyLi, zipList))
# print(zipList)
# print(zipDict)
# zipList2 = list(zipDict.values())
# zipList3 = []

# Output: {0: ('30004',), 1: ('07652',),...

'''Convert Dict Values into list of Tuples'''
# zipList2 = list(zipDict.values())
# print(zipList2)
