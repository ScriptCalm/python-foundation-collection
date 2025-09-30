
# Task 10.1.1

class Products: ############################################### Class Product ################################################
    def __init__ (self, ID, name, price):
        self.ID = ID
        self.name = name
        self.price = price
############################################################################################################################
        
    def printProd(self):
        print(
            'ID:', self.ID,
            ', Name:', self.name,
            ', Price: £', self.price)

class exceptTry: ############################################### Class exceptTry #############################################
    def __init__(self, ID, name, price, userInput):
        super().__init_(ID, name, price)
        self.userInput = userInput
############################################################################################################################
        
    def selectID(x): # except conditions for selecting the product ID
        while True:
            try:
                userInput = int(input(x))
                if userInput > len(productsList) or userInput <1:
                    print(f'You must enter an existing product ID (between 1 and {len(productsList)}).')
                    continue
            except ValueError:
                print('You must enter a numerical value.')
            else:
                return userInput
                break

    def selectQty(x): # except conditions for selecting the Qty
        while True:
            try:
                userInput = int(input(x))
                if userInput > 10:
                    print('You can select a maximum quantity of 10 units at once.')
                    continue
                else:
                    if userInput <0:
                        print('You can select a minimum quantity of 0, if you selected the wrong product.')
                        continue
            except ValueError:
                print('You must enter a numerical value.')

            else:
                return userInput
                break

    def anotherProduct(x): # except contidions for choosing if add more products or exit
        while True:
            userInput = str(input(x))
            if userInput.lower() not in ('y', 'n'):
                print('You must enter Y or N.')
                continue
            else:
                return userInput
                break

class Action: ############################################### Class Action #################################################
    def __init__(self, ID, name, price, userInput, takeQty, productTotal):
        super().__init__(ID, name, price, userInput)
        self.takeQty = takeQty
        self.productTotal = productTotal
############################################################################################################################
        
    def myFunction(): # function for interaction with the user
        while True:
            #call function for print products list
            print()
            print('Please select from our products:')
            print()
            a1.printProd()
            a2.printProd()
            a3.printProd()
            a4.printProd()
            a5.printProd()
            a6.printProd()
            a7.printProd()
            a8.printProd()
            a9.printProd()
            a10.printProd()
            print()
            a = exceptTry.selectID('Select a product by ID: ') # call exceptTry.selecID()
            for i in productsList:    
                if i.ID == a:
                    print("You have selected", i.name)
                    takeQty = exceptTry.selectQty(f'Please select the quantity for {i.name}: ')
                    productTotal = round(i.price * takeQty, 2)
                    print('You have added ', takeQty, 'x', i.name, 'to your basket.')
                    basketList.append(productTotal)
                    print(f'Your total so far: £', sum(basketList))
                    print()

            print('Would you like to add another product to your basket?')        
            addMore = exceptTry.anotherProduct('Enter (Y) for Yes, or (N) to exit: ') 
            if addMore.lower() in 'no':
                print()
                print('Your final total amount is: £', sum(basketList))
                print('Thank you for your business!')
                break
            elif addMore.lower() in 'yes':
                continue


#create objects    
a1 = Products(1, 'Plate', 5.2)
a2 = Products(2, 'Fork', 1.2)
a3 = Products(3, 'Spoon', 1.5)
a4 = Products(4, 'Water Jug', 8.5)
a5 = Products(5, 'Knife', 2.1)
a6 = Products(6, 'Tray', 4.8)
a7 = Products(7, 'Mug', 5.25)
a8 = Products(8, 'Paper Towel', 1.52)
a9 = Products(9, 'Electric Kettle', 15.7)
a10 = Products(10, 'Cutting Board', 5.2)

#objects list for products
productsList = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]

#objects list basket prices
basketList = []

print()
print('Welcom to Our Store!')
Action.myFunction()
