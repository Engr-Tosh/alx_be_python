#Creating a simple bank account class

#Define the bank acoount class
class BankAccount:
    #Use __init__ method to initialize acc blc attribute
    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.initial_balance = 0     #Default value of bank acc blc
        
    
    #Now to practice encapsulation behaviour
    def deposit(self, amount):
        #This method should add a specific amount to account balance
        return self.account_balance + amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            return True
        else:
            return False
    
    def current_balance(self):
        new_balance = self.initial_balance + self.account_balance
        return new_balance
        

    def display_balance(self):
        print(f"Current Balance: {self.current_balance()}")
        