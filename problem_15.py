"""
15. Imagine you are designing a banking application. What would a
customer look like? What attributes would she have? What methods
would she have?
"""
class Customer():
    
    def  __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def with_draw(self, amount):
        if amount>self.balance:
            raise RuntimeError('Amount greater than available balance')
        self.balance = self.balance-amount
        return self.balance
    
    def deposit(self, amount):
        self.balance = self.balance+amount
        return self.balance
customer_one = Customer("sina", 20, 1500)
print(f"amount remaining after withdrawing {200} is: {customer_one.with_draw(200)}")
print(customer_one.deposit(200))