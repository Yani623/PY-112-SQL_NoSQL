"""
ASCII (American Standard Code for Information Interchange), is a character encoding standard for electronic communication. ASCII codes represent text in computers, telecommunications equipment, and other devices.
There is a function for finding the ascii value of a character here: https://docs.python.org/3/library/functions.html
Write a function that asks the user for input, and then computes the sum of all the ascii values of the characters.
"hello" -> 104 + 101 + 108 + 108 + 111 = 532
Part 2: Given a list of words (from user input) determine which word has the highest ascii value.
"""

# name = input("What is your name: ")




# def sumAscii(str):
#     sum1 = 0
#     for x in str:
#         sum1 += ord(x)

#     return sum1

# # sumAscii(name)
# # print(sumAscii(name))

# ### Dominic's Solution:
# ### def ascii(str): return sum(ord(x) for x in str)


# def maxAscii():
#     dayMood = input("In a full sentence, please type how your day is going: ")
#     li1 = dayMood.split()
#     # print(li1)
#     li2 = list(map(sumAscii, li1))
#     # print(li2)
#     maxSums = max(li2)
#     maxAscii = li2.index(maxSums)
#     maxAscii2 = li1[maxAscii]
#     print(maxAscii2)

# maxAscii()


# def wordList(li):
#     for x in range(len(li)):
#         sums = sumAscii(li[x])
        
#     print(li)
#     maxSums = max(li)
#     maxAscii = li.index(maxSums)
#     maxAscii2 = li[maxAscii]
#     return maxAscii2

# wordList(li1)
# print(wordList(li1))











""" 
Analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.
Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.
Sample Inputs:
hello -> True
nono -> False
sunday -> False
racecar -> False
"""

# def double_letters(str):
#     for x in range(len(str)-1):
#         if str[x] == str[x+1]:
#             return True
        
#     return False

# double_letters("hello")
# print(double_letters("hello"))

"""
write a program that prints the following
```
*
* *
* * *
* * * *
* * * * *
* * * * * 
* * * *
* * *
* *
*
``
1) do it using a for loop 
2) do it using a list comp. 
part 2:
replace the middle of any odd numbered row with a smiley emoji 😊 in the middle
"""
#Part 1a:

# for x in range(1,6):
#     print("*" * (x+1))
    
# for x in range(0,6):
#     print("*" * (5-x))   


#Part 1b:


#Part 2:

# star_list = ["*", "*", "*", "*", "*"]
# import emoji
# for x in range(1, 6):
#     if x == 1:
#         print("😊")
#     if x > 0 and x % 2 != 0:
#         print("*" * int((x + 1)/ 2), "😊", "*" * int((x + 1)/ 2))
    
#     else:
#         print("*" * (x))








# def smiley():
#     for i in range(5):
#         if (i%2 != 0):
#             # result = ("*"*(i+1)/2) + ":blush:" +("*"*(i+1)/2)
#             print(("*"*int((i+1)/2)) , ":blush:" , ("*" *int((i+1)/2)))
#         else:
#             print("*"*(i+1))
#     for i in range(5):
#         if (i%2 != 0):
#             # result =("*"*(5-i)/2)+":blush:"+ ("*"*(5-i)/2)
#             print(("*"*i(nt(5-i)/2), ":blush:", ("*"*int(5-i)/2))
#         else:
#             print("*"*(5-i))
# smiley()


# def smiley():
#     for i in range(5):
#         if (i%2 != 0):
#             result = ("*")*(i+1) + "😊" + ("*")*(i+1)
#             print(result)
#         else:
#             print("*"*(i+1))
#     for i in range(5):
#         if (i%2 != 0):
#             result =("*")*(5-i) + "😊" + ("*")*(5-i)
#             print(result)
#         else:
#             print("*"*(5-i))
# smiley()



import csv
with open('dog_data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))