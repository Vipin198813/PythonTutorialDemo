"""Rule - if multiple except blocks are mentioned, then which is matched first will be executed and other which are available below the
matched except blocks are avoided. """

try:
    l = [1,2,3,5,56,7]
    l[2]
    a = 10
    b = 0
    c = a/b

except IndexError as e:
     print(e)

except ZeroDivisionError as e:
    print(e)

except Exception as e:
    print(e)

else:
    print("Everything is fine")

finally:
    print("Complete program is executed.")


# RAISE KEYWORD
"""
Raise keyword is used to explicitly trigger an exception. This is useful when you want to indicate that an error has 
occurred in your program and handle it appropriately. 
"""
y=5
try:
    if y == 4:
        raise FileNotFoundError("Entered file is not present")

except Exception as e:
    print(e)
