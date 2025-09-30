
# Task 6.4.3
import sys # Import sys module

while True:
      userInput = str(input("Enter Y to quit."))
      if userInput == 'Y' or userInput == 'y': # Condition for executing sys.exit
            sys.exit('Goodbye') # SystemExit: Goodbye
            break
      else:
            if userInput != 'Y' and userInput != 'y':
                  continue
            
