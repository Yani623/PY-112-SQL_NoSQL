import statistics

# numList = [89,89,89,93,88,86,88,91,88]
# # numList.sort()
# # print(numList)
# Mode = statistics.mode(numList)
# print(Mode)


# def calcMedian(numList = [88,89,90,93,84,86,88,91,88,87]):
#     numList.sort()
#     print(numList)

# calcMedian()
# print(calcMedian())


import statistics

# print(statistics.median(numList))


# def calcMedian(li=[]):
#     li.sort()
#     middleTwo = []
#     if len(li)%2 == 0:
#         for x in range(len(li)):
#             if x == len(li)/2:
#                 middleTwo.append(li[x])

#             elif x == ((len(li)/2) + 1):
#                 middleTwo.append(li[x])
                
#         median = (middleTwo[0] + middleTwo[1]) / 2

#     elif len(li) % 2 != 0:
#         middle =int((len(li)/2) - .5)
#         median = li[middle]

#     print(median)
        
#     # else:
#     #     print(li[(len(li)/2)+1])

# calcMedian(numList)
numList = [89,89,89,93,88,86,88,91,88]
#set(numList) = {86, 88, 89, 91, 93}

# def calcMode(li=[]):
#     setli = set(li)
#     setli = list(setli)
#     print(setli)
#     count = []
#     mode = []
#     for x in setli:
#         count.append(li.count(x))
#     print(count)
#     maxCount = max(count)
#     for i in range(len(count)):
#         if count[i] == maxCount:
#             mode.append(setli.index(i))
#     mode = str(mode)
#     print(mode)
# calcMode(numList)

