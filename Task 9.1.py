
# Task 9.1

a = int(input('Please enter the first number: '))
b = int(input('Please enter the second number: '))
c = int(input('Please enter the third number: '))
print(' ') # Space

def sumNumber(a, b, c):     # First function
    d = [a, b, c]
    print('The sum of the numbers is:', sum(d))

def smallNumber(a, b, c):    # Second function
    d = [a, b, c]
    print('The smallest number is:',min(d))

def squareNumber(x):         # Third function
    s = pow(x, 2)
    print(f'The square number for {x} is:', s)
    

sumNumber(a, b, c)
smallNumber(a, b, c)

print(' ') # Space

squareNumber(a)
squareNumber(b)
squareNumber(c)



