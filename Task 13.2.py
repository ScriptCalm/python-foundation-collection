
# Task 13.2

products = {
    'Bread': 0.95,
    'Milk': 1.05,
    'Cheddar cheese': 2.5,
    'Tomatoes': 1.05,
    'Sugar': 0.8
    }

print(products)
print(' ') # Space

# Change the price for bread ########
# Print the old price for bread
print('Old price for bread is £', products['Bread'])

# Print price is going up
print('The price of bread is going up!')

# Update the price or bread
products['Bread'] = 1.09

# Print the new price of bread
print('New price for bread is £', products['Bread'])

print(' ') # Space

# Change price for milk
print('Old price for milk is £', products['Milk'])
print('The price of milk is going up!')
products['Milk'] = 1.35
print('New price for milk is £', products['Milk'])
