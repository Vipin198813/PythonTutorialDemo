"""
Functions are blocks of reusable code that perform a specific task. They allow you to write code once and
use it multiple times, which makes your code more modular, readable, and easier to maintain.

Key Concepts:
Function Definition: Functions are defined using the def keyword, followed by the function name and parentheses ().
                     The code block within every function starts with a colon : and is indented.

Parameters: Functions can accept parameters (also called arguments), which allow you to pass data into the function.

Return Statement: The return statement is used to send back a result from the function to the caller.
                  If no return statement is used, the function returns None by default.

Calling a Function: Once a function is defined, you can call it by using its name followed by parentheses ().
                    If the function requires arguments, you must provide them within the parentheses.
"""
s = "This is python class"
print(len(s))
print(sorted(s))
s1 = s.replace("This", "Python1")
print(s1)