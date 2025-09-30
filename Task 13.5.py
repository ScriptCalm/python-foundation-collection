
# Task 13.5

# Exception handling
def checkInt(x): # function for checking if the inputs are integers
    while True:
        try:
            number = int(input(x))
        except ValueError:
            print('You must enter a whole number (integer).')
            continue
        else:
            return number
            break

def divisionFunction():
    a = checkInt('Enter a number: ') # takes input from user
    b = checkInt('Enter another number: ') # takes the second input from user
    print('Divide the first number by the second:')
    while True:
        try: # open try block
            d = a/b
        except ZeroDivisionError: # handle the zero division error
            print('An error has occurred due to zero division')
            print('The try block will not execute further')
            break
        else:
            print('The division was successful. Result:', d)
            break

divisionFunction() # calling the division function
