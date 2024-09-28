class MeraError(Exception):
    pass

def fun(x,y):
    if y == 0:
        raise MeraError("Error Occurred")
    return x/y

try:
    fun(10,0)
    raise MeraError("This is my another error")

except Exception as e:
    print(e)
