"""
The for loop in Python is a powerful tool used to iterate over a sequence (such as a list, tuple, string,
or range) and execute a block of code for each item in the sequence.
Syntax of for loops:-
for variable in sequence:
    # Code to execute for each item in the sequence

Explanation:
Variable:
A temporary variable that takes the value of the current item in the sequence during each iteration.
sequence:
A collection or sequence of elements that the loop will iterate over (e.g., a list, string, tuple, or range).
Block of code:
The indented code inside the loop runs once for each item in the sequence.

When to use FOR loop - If we know the repetitions in advances then in such case we can use FOR loop
                     - When data is present in sequence.
                      a) Generate sequences using RANGE function - It is a inbuilt function.
                            eg: RANGE(start, end, gap or step) - Last value is excluded.
                      b) List, String, Tuple
When to use WHILE loop - If we are not sure about the number of repetitions in advance then in such case we can use
                        WHILE loop
"""
number = list(range(10,1,-2))
print(number)
number1 = tuple(range(1,10,2))
print(number1)
print(type(number))
print(type(number1))

for i in number:
    print(i)
