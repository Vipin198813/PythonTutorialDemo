"""Read(5) function - It means it will read 5 characters from the file.
    At the end of the line, a line break characters is included that is also considered while counting the characters."""
import os

# with open('test.txt','w') as f:
#     f.write("This is first line\n")
#     f.write("This is my second line\n")
#     f.write("This is the third line")

# # lines = ['line1\n', 'line2\n', 'line3\n', 'line4\n']
# with open('test5.txt','r') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)

f = open('test5.txt','r')
line_count = 0
while f.readline():
    line_count = line_count + 1
print(f"No of lines: {line_count}")


"""SEEK and TELL"""

# with open('test5.txt','r') as f:
#     f.readline()
#     print(f.tell())

with open('test5.txt', 'r') as file:
    file.seek(10)  # Move the pointer 10 bytes from the start
    content = file.read()  # Read from the 10th byte onward
    print(content)

"""OS Module Related Information"""
print(os.getcwd())
# os.chdir()
# os.path.join()
# os.mkdir("Vipin1")
# os.makedirs("Vipin1/Vipin2")
print(os.listdir())