
# Task 13.4

products = {
    'Bread': 0.95,
    'Milk': 1.05,
    'Cheddar cheese': 2.5,
    'Tomatoes': 1.05,
    'Sugar': 0.8
    }

print(products)
print(' ') # Space

#### User can add further products and prices to the dictionary

while True: # Creating a loop
    addProduct = str(input('Would you like to add another product? enter Yes or No: ')) # input from user
    if addProduct == 'Yes' or addProduct == 'yes': # Condition for adding a new product
        enterProduct = str(input('Enter the next product name: ')) # input the product name
        enterPrice = float(input(f'Enter the price for {enterProduct}: ')) # input the price for new product
        products[enterProduct] = enterPrice # add the new product to dictionary
        print(' ') # Space
        print('Product successfully added!')
        print(products)
        print(' ') # Space
        
    elif addProduct == 'No' or addProduct == 'no': # Condition for not adding a new product
        print(' ') # Space
        print('Thank you for your business!')
        break
    
    else: #Condition for invalid input
        if addProduct != 'Yes' or addProduct != 'yes' or addProduct != 'No' or addProduct != 'no':
            print('You must enter Yes or No only.')
        continue
