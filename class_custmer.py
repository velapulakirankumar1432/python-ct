class Customer:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Balance:", self.balance)
    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited. New balance:", self.balance)
    def withdraw(self, amount):
        self.balance = max(0, self.balance - amount)  # balance cannot go below 0
        print(amount, "withdrawn. Remaining balance:", self.balance")
c1 = Customer("Rahul", 25, 5000)
c1.display()
c1.deposit(2000)
c1.withdraw(3000)
c1.display()
