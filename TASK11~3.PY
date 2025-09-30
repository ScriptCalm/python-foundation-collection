
# Task 11.2.a

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def print_balance(self):
        print("Account balance for account " + self.account_number + " is: " + str(self.balance))
        
account1 = BankAccount("123456789", 1000.00)
account2 = BankAccount("012345678", 200.00) # new account object
account3 = BankAccount("901234567", -50.00) # new account object

# calling the print function for all 3 objects
account1.print_balance()
account2.print_balance()
account3.print_balance()
