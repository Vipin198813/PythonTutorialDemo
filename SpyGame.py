#[1,0,1,0,7,8,7,8] --> Return True
#[1,7,1,0,7,8,7,8] --> Return False

def spy_game(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

result = spy_game([1,7,1,0,7,8,7,8])
print(result)

