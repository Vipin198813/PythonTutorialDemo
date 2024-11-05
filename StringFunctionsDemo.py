#len() - Return the length of the string. It counts every character written inside the double quotes even  white spaces also.
str = "python prog"
print(len(str))

#Capitalize(): Return the exact copy of the string with only the first letter in upper case
Str = "welcome to the python world"
print(Str.capitalize())

# find(sub[,start[,end]]): This function is used to search the first occurrence of the substring in the given string. It returns the
#   index at which the substring starts. It returns -1 if the substring does not occur in the given string.
S = "Mammals"
print(S.find('md'))
print(S.find('ma',2,6))

#isalnum(): Return True if the string contain only letters and digits. It returns False, if the string contains any special
# characters like _, @, &, *,#
print("Python12".isalnum())    # True
print("Python12%#".isalnum())    # False

#isalpha(): Return True if all the characters of the given string are alphabets. Otherwise return False.
print("Python12".isalpha())    # False
print("Python".isalpha())    # True

#isdigit(): Return True if all the characters of the given string are digits. Otherwise return False.
print("Python12".isdigit())    # False
print("234253423423".isdigit())    # True

#lower(): Return the exact copy of the string with all the letters in lowercase.
print("pPTUSGSD235345#".lower())

#islower(): Return True is all the characters in the given string are in lowercase. Otherwise return False.
print("pwaerkjhreqwr235345#".islower())

#upper(): Return the exact copy of the string with all the letters in uppercase.
print("ajhdkaskasd#".upper())

#isupper(): Return True is all the characters in the given string are in uppercase. Otherwise return False.
print("PPTUSGSD235345#".isupper())

#lstrip(): Return the string after removing the spaces on the left of the given string.
String1 = "    Welcome to python world     "
print(String1.lstrip())
String2 = "Welcome to python world     "
print(String2.lstrip("We"))

#rstrip(): Return the string after removing the spaces on the right of the given string.
String1 = "    Welcome to python world     "
print(String1.rstrip())

#isspace(): Return True if the string contains only white spaces and False even if it contains once character.
String1 = "   "
print(String1.isspace())
print("p".isspace())# True

#istitle(): Return True if the string is title cased(First character of every word should be capital). Otherwise return, False.
Str = "The Green Revolution"
print(Str.istitle())

#replace(old,new): The function replaces all the occurrences of the old string with the new string.
Str = "Hello Wold"
print(Str.replace('Hello','%'))

#Join(): Return a string in which the sequence(list, tuple or string) have been joined by a separator.
Str1 = ('Jan','Feb','March')
Str2 = '&'
print(Str2.join(Str1))

#swapcase(): Return the string with case change
Str1 = ('JanlskdfUTIUYSUD')
print(Str1.swapcase())

#split([sep[,maxsplit]]):
#The function splits the string into substring using separator. Always return the result in the form of list type.
Str1 = "I Love Python Programming Language"
print(Str1.split('o'))

#Count the number of times a characters present in the string.
String1 = input("Enter any String:  ")
C = input("Enter character to check frequency: ")
count = 0
for i in String1:
    if i == C:
        count+=1
print(C, "Occurs", count, "times")

# Check if the string is palindrome or not
#Method: 1
Original = input("Enter a string: ")
Reverse = Original[::-1]
if Original == Reverse:
    print("String is palindrome")
else:
    print("String is not a palindrome")

#Method 2:
Original = input("Enter a string: ")
Reverse = ""
for i in range(len(Original)-1,-1,-1):
    Reverse = Reverse + Original[i]
print(Reverse)


#Program in python to reverse the alternate words in a string:
#"How are you
s = input("Enter a string: ")
words = s.split()
# "I love python programming language" After applying split function ['I', 'love','python','programming','language']
for index in range(1, len(words),2):
    rev = ""
    for ch in words[index]:
        rev = ch + rev
    words[index] = rev
reverse = " ".join(words)
print("After reversing string of alternate words")
print(reverse)

#Program to replace all vowels in a string with '*'
String = input("Enter a string: ")
for i in String:
    if i.lower() in 'aeiou':
        print('*',end="")
    else:
        print(i,end="")





