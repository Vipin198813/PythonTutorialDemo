# String Creation using Single Quotes
str1 = 'Hello Python'
print(str1)

# String Creation using double Quotes
MyStr = "HELLO PYTHON"
print(MyStr)

# String Creation using Triple Quotes
mystr = '''Hello 
Python
'''
print(mystr)

mystr = ('''Happy 
Monday 
Everyone
''')
print(mystr)

mystr1 = "Woooo "
mystr1 = mystr1 * 5
print(mystr1)
print(len(mystr1))

print("############### STRING INDEXING  ################")
"""----------------Forward Indexing------------------------>
0   1   2   3   4   5   6   7   8   9  10   11      #Note - Only 1 space is present between Hello and Python. Ignore Others
H   E   L   L   O       P   Y   T   H   O   N
-12-11-10  -9  -8  -7  -6  -5  -4  -3  -2  -1
<----------------Backward Indexing-----------------------    
"""
Str1 = "Hello Python"
#1.Print first character in the string.
print(str1[0])    #Print first character in the string.

#2.Print the last characters of the string
print(Str1[len(str1)-1])

#3.Last character of the string
print(Str1[-1])

#4.Fetch 7th character from the string
print(Str1[6])

print("########### STRING SLICING #################")
# Fetch characters from 0 to 5 index location excluding character at index 5.
print(Str1[0:5])

print(Str1[:5])   # Output: "Hello" (from start to index 4)
print(Str1[7:])   # Output: "World!" (from index 7 to end)

print(Str1[0:13:2])  # Output: "Hlo ol!" (characters from index 0 to 12, stepping by 2)

str2 = "Hello, World!"
print(str2[-6:-2])  # Output: "World" (from index -6 to -2)
print(str2[-6:])    # Output: "World!" (from index -6 to end)
print(str2[:-1])    # Output: "Hello, World" (from start to index -1)
print(str2[-1:-13:-2])  # Output: "!lo olH" (characters from the end stepping backwards)

print("\n")
print("$$$$$$$$$$$ STRING SLICING EXAMPLES $$$$$$$$$$$$$$$$$$")
#str[Start:Stop:Step]
#Note:
# If Step value is positive, then move in forward direction.
# If Step value is negative, then move in backward direction.
S = "PYTHON PROGRAMMING"
print(S[::-2])   # We have to move in backward direction i.e.: GIMROPNHY
print(S[2:3])    #If step value is not provided, then by default it is considered as 1 only. #T
print(S[2:3:-1])  #As per start and stop we have to move in forward direction, but as per step we have to move in back
                  # backward direction. There is mismatch in direction, so it will return an empty string.
print(S[-15:-16])  #Start and stop indicate the movement in backward direction, but as the step value is not provided then we consider
                    # to move in forward direction. Now there is a mismatch in the movement then it will again return empty string. \
print(S[-15:-16:-1]) # H
print(S[-6:7:-2])    #AGR
print(S[4:-8])         #ON PRO
print(S[9:-10])      #Return an empty string
print(S[9:-10:-1])      #O
print(S[22::-6])        #GRN
print(S[2:-22:-1])      #TYP
print(S[15::-2])        #IMROPNHY
print(S[-15::-2])       #HY
print(S[7:-1])          #PROGRAMMIN









