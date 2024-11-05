class Sample():
    pass
mySample = Sample()
print(mySample)

class Book():
    def __init__(self,author,title,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}"

b = Book("Python Rocks","Joe",200)
print(b)
print(str(b))

