def mul(a):
    def mul1(b):
        return a+b
    return mul1

result = mul(2)(3)
print(result)