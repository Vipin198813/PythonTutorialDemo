class card:
    def __init__(self,suite,rank):
        self.suite = suite
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suite

two_hearts = card("Heart","Two")
print(two_hearts)