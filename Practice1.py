#lesser of two even(2,4) --> Return 2
#lesser of two even(2,5) --> Return 5

def lesser_of_two_even(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        #One number or both numbers are odd
        return max(a,b)

result = lesser_of_two_even(14,12)
print(result)

