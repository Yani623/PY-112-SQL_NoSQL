'''
Plaintext: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
    part 1 Write a function that computes the cesear cipher of a message (example above)
    part 2 BONUS Write a function that takes a number and a direction (left or right) and creates a cipher from these parameters i.e. n=6, shift=right
    Plaintext: A Dog Ciphertext: G JUM
'''

text ="THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"


'''Shift of Three to The Left'''
# def Ciphertext(str1 = ""):
#     li1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     li2 = li1[3:] + li1[:3]
#     newDict = {li2[i]: li1[i] for i in range(len(li1))}

#     strLi = list(str1)
#     cipherLi = []
#     for x in strLi:
#         if x == " ":
#             cipherLi.append(x)
#         elif x.isalpha():
#             cipherLi.append(newDict.get(x))

#     cipherStr = ''.join(cipherLi)
#     print(cipherStr)


'''Using User Input to Rotate'''
def Ciphertext(str1 = ""):
    li1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    in1 = int(input("Enter the number you want to rotate your alphabet by:"))
    in2 = input("Do you want it to rotate left, or right?").lower().strip()
    
    if in2 == "left":
        li2 = li1[in1:] + li1[:in1]
        
    elif in2 == "right":
        li2 = li1[(len(li1) - in1 - 1):] + li1[:len(li1) - in1 - 1]
    
    newDict = {li2[i]: li1[i] for i in range(len(li1))}

    strLi = list(str1)
    cipherLi = []
    for x in strLi:
        if x == " ":
            cipherLi.append(x)
        elif x.isalpha():
            cipherLi.append(newDict.get(x))

    cipherStr = ''.join(cipherLi)
    print(cipherStr)
            

Ciphertext(text)



