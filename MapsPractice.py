def square(x):
    return x**2
my_nums = [1,2,3,4,5,7,8]
for item in map(square,my_nums):
    print(item)
result = list(map(square,my_nums))
print(result)

def splicer(mystring):
    if(len(mystring)%2 == 0):
        return "EVEN"
    else:
        return mystring[0]

names = ['Vipin','Shiva','Deva']
print(list(map(splicer,names)))
