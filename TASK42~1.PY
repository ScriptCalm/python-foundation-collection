
# Task 4.2

# Option 1: use round() function at the print statement
print('Output limited using (round) function at print statement:')
x = 19.93  
y = 20.00  
z = y - x
print(round(z, 2))

print(' ') # Space

print('''Called at a later stage the decimal limitation
will not hold, unless the 'round' function is used again ''')
print(z + 1) # If z is called later the decimal limitation will not hold
