
# Task 11.2.c

class BankAccount:
    def __init__(self, name, gender, account_number, balance):
        self.name = name
        self.gender = gender  # gender added for dividing in between him/her
        self.account_number = account_number
        self.balance = balance

    def print_balance(self):
        print("Account balance for " + self.name +
              "'s account " + self.account_number +
              " is: " + str(self.balance))

    def print_name(self):
        print("Account holder for account " + self.account_number +
              " is: " + self.name)

    def withdraw(self, amountDeduct):  # defining withraw function
        self.balance = self.balance - amountDeduct
        if self.gender == 'female': # dividing in between him/her
            print(self.name + ' is withdrawing ' + str(amountDeduct) + ' from her account')
            print('Her new balance is as follows:')
        else:
            print(self.name + ' is withdrawing ' + str(amountDeduct) + ' from his account')
            print('His new balance is as follows:')
            
        print("Account balance for " + self.name +
                "'s account " + self.account_number +
                " is: " + str(self.balance))

    def deposit(self, amountAdded): # defining deposit function
        self.balance = self.balance + amountAdded
        
        if self.gender == 'female': # dividing in between him/her
            print(self.name + ' is depositing ' + str(amountAdded) + ' into her account')
            print('Her new balance is as follows:')
            
        else:
            print(self.name + ' is depositing ' + str(amountAdded) + ' into his account')
            print('His new balance is as follows:')

        print("Account balance for " + self.name +
                "'s account " + self.account_number +
                " is: " + str(self.balance))

# creating objects          
account1 = BankAccount("Alice", "female", "123456789", 1000.00)
account2 = BankAccount("Bob", "male", "012345678", 200.00)
account3 = BankAccount("Jane", "female", "901234567", -50.00)

# calling print_balance function on the objects
account1.print_balance()
account2.print_balance()
account3.print_balance()

#print('Calling the print_name function')
#account1.print_name()
#account2.print_name()
#account3.print_name()
print(' ') # space

account1.withdraw(50) # Call withdraw function
print(' ') # space

account2.deposit(200) # Call deposit function
