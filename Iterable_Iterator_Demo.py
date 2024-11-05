import sys
l1 = range(10000000000)
print(sys.getsizeof(l1))

# for i in range(5):    #Iterations - Fetching one value at a time from the location where they are stored is called iterations.
#     print(i)          # Iterables are those on which we can perform iterations. 
#
# l2 = [1,4,5,3,5,5,3,5,6]   #Iterations is possible on list datatype
# for i in l2:
#     print(i)

l3 = (1,4,5,3,5,5,3,5,6)        #Iterations is possible on tuple datatype
for i in l3:
    print(i)
#
# i = 454435345             # iterations are not possible on Integer datatype
# for j in i:
#     print(i)