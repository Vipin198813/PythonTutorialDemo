"""
In Python, a dictionary is a built-in data type that represents a collection of key-value pairs. Dictionaries are versatile and
commonly used for storing and managing data where each item has a unique identifier (the key) and an associated value.

Key Characteristics: -
a) Unordered: Dictionaries do not maintain the order of items. As of Python 3.7, dictionaries preserve insertion order,
              but you should not rely on this for logic that depends on order.
b) Mutable: You can change, add, or remove items after the dictionary is created.
c) Keys Must Be Unique: Each key in a dictionary must be unique. If a duplicate key is used, the value associated with the key will
            be updated.
d) Keys Must Be Immutable: Dictionary keys must be of an immutable type, such as strings, numbers, or tuples
                           (containing only immutable elements).
"""

d = {"abc":"1","abc":"2"}
#   Keys validations:
#   Keys are Unique and Immutable
#   Immutable - Allowed for Keys (string, int, boolean, tuple).
#   Mutable - Not allowed for Keys (List, Set

#   Values Validations -
#   Values can be non unique and be be changed

print(d["abc"])
d["abc"] = "Vipin"
print(d["abc"])
print(d)
python_my_dict = {'one': 1, 'two': 2, 'three': 3}
print(python_my_dict.get('four', 4))
print(len(python_my_dict))



