class AccountHolder:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
    def display(self):
        print("Name:", self.name, "Acc No:", self.acc_no, "Balance:", self.balance)
    def deposit(self, amt):
        self.balance += amt
        print("Deposited:", amt, "New balance:", self.balance)
    def withdraw(self, amt):
        withdrawn = min(self.balance, amt)  
        self.balance -= withdrawn
        print("Withdrawn:", withdrawn, "Remaining balance:", self.balance)
acc = AccountHolder("Rahul", 101, 5000)
acc.display()
acc.deposit(2000)
acc.withdraw(8000)  
acc.display()
