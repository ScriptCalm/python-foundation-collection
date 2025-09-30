
# Task 6.3
   
while True: # Creating a loop
    try:
        number = int(input('Please enter an integer number: '))
    except ValueError: # Check if the value is an integer
        print('You must enter a whole number (integer).')
        continue
    if number % 7 == 0: # check if the number is divisible by 7
        print('Divisible by 7')
    else:
        print('Not divisible by 7')
    break
    
    

