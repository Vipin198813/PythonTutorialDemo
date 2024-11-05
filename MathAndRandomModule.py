import math
value = 4.51
print(math.floor(value))
print(math.ceil(value))
print(round(value))
print(math.e)
print(math.log(100,9))
print(math.sin(90))
print(math.degrees(math.pi / 2))

import random
print(random.randint(1,100))
mylist = list(range(0,20))
print(mylist)
print(random.choice(mylist))
#SAMPLE with replacement
print(random.choices(population=mylist,k=10 ))
#SAMPLE without replacement
print(random.sample(population=mylist,k=10 ))
print("original list\n",mylist)
random.shuffle(mylist)
print(mylist)