def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

result = create_cubes(10)
print(result)

for x in create_cubes(10):
    print(x)