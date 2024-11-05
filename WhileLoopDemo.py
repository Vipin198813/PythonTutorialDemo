"""
When to use WHILE LOOP - When the number of iterations are not known to us, then in such scenarios we
can use while loop
We decide the iterations based on some conditions.
        - True condition - Iteration continues
        - False condition - Stop iteration
Conditions:
    - Constant
    - Variables
    - Expression
    e.g: x = 5, x < 5, x+y=5
     In some cases expression remains positive - So to avoid this we have to keep increasing the variable value.
     i.e. Iterations - We have to keep this in mind that while providing conditions we have to keep increasing the variable value.
i = 0
while i < 6:
    print(i)
    i = i+1

i=0
while True:
    print(i)
    if i == 5:
        print("Bhaiya aap to out ho gaye hai.")
        print("Isiliye aapki batting katam ho gayi hai")
        break
    i = i +1
"""


i = 1
count = 1
while i <= 5:
    print(f"Ball number {i}")

    if i == 3:
        print(f" Ball number {i} wide hai, isliye isko count nahi karenge")
        i = i+1
        continue
        count = count + 1  # This statement is skipped once the above conditions become true

    print(f"Legal ball number {count}")
    count = count + 1
    i = i + 1

if count >= 7:
    print("Over is completed")
else:
    print("Over is not completed")