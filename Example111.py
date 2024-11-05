class Account():
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self,dep_amount):
        self.balance = self.balance + dep_amount
        print(f"Added {dep_amount} to the balance")
    def withdrawal(self,wd_amount):
        if self.balance >= wd_amount:
            self.balance = self.balance - wd_amount
            print("Withdrawal Accepted")
        else:
            print("Not enough balance")

    def __str__(self):
        return f"Owner :{self.owner} \nBalance: {self.balance}"

a = Account("Sam", 500)
print(a.owner)
print(a.balance)

print(a)

dep_amount = print(a.deposit(100))

print(a.withdrawal(600))
print(a)

print(a.withdrawal(1))