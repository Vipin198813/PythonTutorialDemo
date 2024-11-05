def myfunc(*args):
    for i in args:
        print(i)
    # Returns 5% of the sum of a and b
    return sum(args) * 0.05

print(myfunc(10,20,30,50,46,75))

def myfunc(**kwargs):
    print(kwargs)

myfunc(fruit= 'Apple', Vege = 'Potato')


def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}".format(args[0], kwargs['food']))

myfunc(10,29,20,40,30,30,fruit = 'Orange', food= 'Eggs', Sweets = 'Ladoo')


def myfunc(*args):
    for n in args:
        if n%2 == 0:
            return list(args)
    print(n)

result = myfunc(1,2,3,4,5,6,7,8,9,10)
print(result)