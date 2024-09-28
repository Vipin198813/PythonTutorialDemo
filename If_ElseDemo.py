"""The if-else statement in Python is a fundamental control structure that allows you to execute different
blocks of code based on certain conditions. Here's a basic introduction:
Syntax of if-else:
if condition:
    # Code to execute if the condition is True
else:
    # Code to execute if the condition is False

Explanation:
if statement:
The if statement checks a condition.
If the condition is True, the block of code under the if statement is executed.

else statement:
The else block is optional and executes if the condition in the if statement is False.
This allows you to handle cases where the condition is not met.

KEY POINTS:
Key Points:
Indentation: Python relies on indentation to define the blocks of code. Make sure that the code inside if,
elif, and else blocks is properly indented.

Conditions: Conditions are typically comparisons (e.g., ==, !=, >, <, >=, <=), but they can be any expression
that evaluates to True or False. elif is optional: You can have as many elif statements as needed, or none
at all. The if-else structure is a powerful tool for decision-making in your programs,
allowing you to direct the flow of execution based on different conditions.
elif or else if

"""

grade = 85

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
else:
    print("Grade: F")
