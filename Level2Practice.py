#See the list and return true if 2 consecutive list items are same
def has_33(num):
    for i in range(0,len(num)-1):
        if num[i] ==3 and num [i+1] ==3:
            return True
        else:
            return False
result = has_33([1,2,3,3])
print(result)

def paper_doll(text):
    result = ''
    for char in text:
        result = result + char*3
    return result

result = paper_doll("vipin")
print(result)

