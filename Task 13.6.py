
# Task 13.6

products = {
    'Bread': 0.95,
    'Milk': 1.05,
    'Cheddar cheese': 2.5,
    'Tomatoes': 1.05,
    'Sugar': 0.8
    }

print(products)
print(' ') # Space

####################################################################################################################
####### Functions for exception handling ###########################################################################

def inputProduct(t): # Product input error detection
    while True:
        a = str(input(t)).capitalize() # capitaliza() function to trap case sensitivity issues
        if a in products: # Check if the product is in dictionary already
            print('This product already exists in the dictionary, please enter a new product name.')
            continue
        elif a.isnumeric() == True: # Check if the input is invalid (such as numerical)
            print('You must enter a valid product name (text).')
            continue
        else:
            return a
            break

def inputPrice(t): # Price input error detection
    while True:
        try:
            a = float(input(t))
        except ValueError: # Check if the value inputted is numerical
            print('You must enter a valid price (numerical).')
        else:
            return a
            break
        
####################################################################################################################
####################################################################################################################
        

####### User can add further products and prices to the dictionary #################################################
        
while True: # Creating a loop
    addProduct = str(input('Would you like to add another product? enter Yes or No: ')) # input from user
    
    while addProduct.lower() not in ('yes', 'no'): #Condition for invalid input using while loop
        print('You must enter Yes or No only.')
        break
    
    while addProduct.lower() in 'yes': # Condition for adding a new product using while loop
        enterProduct = inputProduct('Enter the next product name: ') # input the product name
        enterPrice = inputPrice(f'Enter the price for {enterProduct}: ') # input the price for new product
        products[enterProduct] = enterPrice # add the new product to dictionary
       
        print('Product successfully added!')
        print(products)
        break
          
    if addProduct.lower() in 'no': # Condition for not adding a new product using if control statement
        print('Thank you for your business!')
        break    
