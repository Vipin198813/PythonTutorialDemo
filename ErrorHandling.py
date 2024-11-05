def add(n1,n2):
    print(n1+n2)

add(10,20)

try:
    #WANT TO ATTEMPT THIS CODE EVEN IF ANY ERROR OCCUR
    result = 10 + '10'
except:
    print("Something happened!!!")
else:
    print("Addition of number went well")
    print(result)