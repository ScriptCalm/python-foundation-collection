
# Task 9.4.1

def testInput(text): # Function for testing the input as integer
    while True:
        try:
            number = int(input(text))
        except ValueError:
            print('You must enter a whole number (integer).')
        else:
            return number
            break

number_1 = testInput('Enter number 1: ') # Input first no. - global
number_2 = testInput('Enter number 2: ') # Input second no. - global

def swapFunction(a, b): # Function for swapping the numbers
    print(f'Before invoking the swap function, number 1 is: {a} and number 2 is: {b}')
    a, b = b, a # Swapping the numbers
    print(f'After invoking the swap function, number 1 is: {a} and number 2 is: {b}')

swapFunction(number_1, number_2) # Calling the swapping function
