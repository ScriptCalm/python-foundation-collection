
# Task 6.4.4

while True:
      userInput = str(input("Enter Y to quit: "))
      if userInput == 'Y' or userInput == 'y': # Condition for executing exit()
            exit(print('Goodbye')) # exit() function used
            break
      else:
            if userInput != 'Y' and userInput != 'y': # ask to input y again
                  continue
            
