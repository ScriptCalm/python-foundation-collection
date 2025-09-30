
# Task 9.3

# Taking inputs from the user
msg = str(input('Enter your message: '))

while True: # Creating a loop for validity input
    try: # Testing the input
        number = int(input('Enter the number of times you want the message to be printed: '))
        if number < 0: # Testing for nevative numbers
            print('You must enter a positive number.')
            continue
    except ValueError: # Testing for non-numerical inputs
        print('You must enter a numerical value.')
        continue
    else:
        break

# defining a function
def myFunction(y, x):
    for a in range(x): # Creating a loop
        print(y) # Print the msg.

myFunction(msg, number) # Calling the function
    
   
    

