"""
#Arithematic Operators - String cannot be added to an integer value. Both strings should be string.
    a) Additions: Concatenation
                s = "askjfd" and S1 = "wrewerwer"

                s + S1
                "askjfdwrewerwer"
    b) Multiplication: Repetition
                2 * "Vipin"
                "VipinVipin"

# As strings are sequential data types - we can use loops on strings.
# Membership operators in string - IN and NOT IN operators - Used to check if any value or substring is present in our string.
# Relational operators: ==, !=, <, >, <= and >= etc
#Logical Operations: AND, OR and NOT
"""

str1 = "This is a python programming language"
str2 = "Python programming is a good programming language"
# if 'si' in str1:
#     print("Ye string present hai")
# else:
#     print("Ye string present nahi hai")

# if str1 == str2:
#     print("Dono strings same hai")
# else:
#     print("Dono strings same nahi hai. ")
#
print(str1==str2)
print(str1>str2)
if 'p' in str1 and 'tyt' in str2:
    print("Yes both are true")
else:
    print("Both are not true")