
# Task 6.4.2

while True: # Create loop
      userInput = str(input("Enter Y to quit: "))# Takes user input
      if userInput != 'Y' and userInput != 'y': # Create condition
            print('Wrong input.')       
      else:
            print("Goodbye") #if the user entered “Y” or “y”.
            break
      
