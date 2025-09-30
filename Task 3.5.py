
# Task 3.5


print('This program will compute the area of a triangle.')

# Input statement that takes the base size value from the user
tr_base = float(input('Enter the base size of the triangle: '))

# Input statement that takes the height size value from the user
tr_height = float(input('Enter the height size of the triangle: '))

print(' ') # Space

print('Output area for result:') # Dividing between input and output

# 'print’ statement as a mathematical formula.
# Function ‘round’ is used to limit the number of decimals.
print('The area of the triangle is: ',
      round(tr_base * tr_height / 2, 2))
