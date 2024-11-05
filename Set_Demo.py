"""
In Python, a set is a built-in data type that represents an unordered collection of unique elements. Sets are useful when you
need to store items and ensure that there are no duplicates. They also provide efficient operations for checking membership,
adding, and removing items.
You can create a set using curly braces {} or the set() function.
# Using curly braces
my_set = {1, 2, 3, 4, 5}

# Using the set() function
another_set = set([1, 2, 3, 4, 5])

Properties of Sets
Unordered: The items in a set are not stored in any specific order.
Unique: A set does not allow duplicate elements.
Mutable: Sets are mutable, meaning you can add or remove elements after creation.
Iterable: You can iterate over the elements in a set, but you cannot index them.
"""
# # Define two sets
# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
#
# # Union
# union_set = set_a.union(set_b)
# print("Union:", union_set)  # Output: Union: {1, 2, 3, 4, 5, 6}
#
# # Intersection
# intersection_set = set_a.intersection(set_b)
# print("Intersection:", intersection_set)  # Output: Intersection: {3, 4}
#
# # Difference
# difference_set = set_a.difference(set_b)
# print("Difference:", difference_set)  # Output: Difference: {1, 2}
#
# # Symmetric Difference
# symmetric_difference_set = set_a.symmetric_difference(set_b)
# print("Symmetric Difference:", symmetric_difference_set)  # Output: Symmetric Difference: {1, 2, 5, 6}

s = {3,4,6,3,"Vipin","Python"}
print(s)
#print(s[1]) # As the index is not fixed, so element access through index is not possible
s.add("Damco")
print(s)
# s.add([3,2,7])  #Not allowed to add List datatype
# s.add({4,8,4,3})  #Not allowed to add set datatypes
print(s)
s.remove("Damco")     #This function is used to remove an element from set datatype.
print(s)

