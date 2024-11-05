"""Break and Continue - These are built in keywords reserved for doing specific task.
        They manage the flow of loops
    Break Statement - We have a list = [1,3,5,7,9,11,13] - If we are search for an element '7' then we
                start searching the elements from 1st position and stop our search once we reach to the
                required element.
    Continue Statement - In a sequence if we don't want to execute our code for a particular conditions, then
                    in such case we use continue statement.
"""
# Break
l = [1,2,3,4,5,6,7,8]
for i in l:
    if i==4:
        print("condition true ho gayi hai, 4 mil chuka hai")
        break
    print(i)
else:
    print("condition false ho gayi hai, l me 4 nahi mila hai")

#Continue
l = [1,2,3,"Ramesh",5,6]
for i in l:
    print("Aapko Diwali bonus milne wala hai")
    print(i)
    if i == "Ramesh":
        print("Aap company leave kar chuke hai, aapko bonus nahi milega")
        continue
    print("5000 Rs aapko bhej diye jayenge")

