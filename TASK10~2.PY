
# Task 10.1.2

print('There are four products ot offer: ')
print('1: Banana, £1.99')
print('2: Apple, £0.99')
print('3: Kiwi, £2.99')
print('4: Orange, £1.50')
userInput = int(input('Enter the product ID or press -1 to exit: '))
total = 0.0

while userInput != -1:
    quantity = int(input('Enter the quantity: '))
    if userInput == 1:
        print('You have selected Banana')
        total = total + (1.99 * quantity)
    elif userInput == 2:
        print('You have selected Apple')
        total = total + (0.99 * quantity)
    elif (userInput == 3):
        print('You have selected Kiwi')
        total = total + (0.50 * quantity)
    elif (userInput == 4):
        print('You have selected Orange')
        total = total + (1.50 * quantity)
    else:
        print('Invalid Product ID')
        print('There are four products of offer: ')
    print('1: Banana, £1.99')
    print('2: Apple, £0.99')
    print('3: Kiwi, £2.99')
    print('4: Orange, £1.50')
    userInput = int(input('Enter the product ID of press -1 to exit: '))

print('Your total shopping amount is: £ ', total)
