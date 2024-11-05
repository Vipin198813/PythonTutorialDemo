"""
In Python, a list is a data structure that allows you to store a collection of items in a single variable. Lists are ordered, mutable,
and allow duplicate elements. Here's a basic example of how to create and use lists in Python:
# Creating a list
my_list = [1, 2, 3, 4, 5] - Homogenous List

# Lists can also contain different data types
mixed_list = [1, "Hello", 3.14, True, (1, 3, 56)] - Heterogeneous list

Nested_List = [1, "Hello", 3.14, True, [1, 3, 56]] - Nested list

Also, we can use list() function to create a list.
e.g: list((1,2,34,"Vipin", 4.56)) - We call this as type conversion

Update list:
  a) Add one element at the end of the list - use append() function
  b) Add 2 elements at the end of the list  - use extend() function  e.g: l.extend([2,3,4,5,6])
  c) Add element at particular position of the list

Delete element from list:
    a) Delete the last element of the list - pop() function
    b) Delete the element present at particular index - del list[index_number]
    c) Some Value from the list - list.remove("Value_you_want_to_remove) - It remove the first occurrence of the value
    d) Delete all the elements from the list i.e. Empty String - l.clear() - It delete all the elements from the list.
    e) Delete the whole list itself - del list_name

"""
l1 = list((1,2,34,"Vipin", 4.56))
print(l1)
l1.extend([4,5,3,5,6,])
print(l1)







