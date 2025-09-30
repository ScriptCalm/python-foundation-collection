
# Task 11.2.b

class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name # added new attribute, name
        self.account_number = account_number
        self.balance = balance

    def print_balance(self):
        print("Account balance for " + self.name + # modified print_balance
              "'s account " + self.account_number +
              " is: " + str(self.balance))

    def print_name(self): # added new function called print_name
        print("Account holder for account " + self.account_number +
              " is: " + self.name)
        
account1 = BankAccount("Alice", "123456789", 1000.00)
account2 = BankAccount("Bob", "012345678", 200.00)
account3 = BankAccount("Jane", "901234567", -50.00)

print('Creating three bank account objects and calling the print_balance function:')
account1.print_balance()
account2.print_balance()
account3.print_balance()

print(' ') #space

# Calling the new created function
print('Calling the print_name function')
account1.print_name()
account2.print_name()
account3.print_name()


