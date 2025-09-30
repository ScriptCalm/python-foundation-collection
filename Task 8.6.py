
# Task 8.6

# defining a function that takes the user input    
def mainFunction(): # Creating the main function
    userInput = str(input('Please enter some input: ')) # Takes user input

    # print statement with the result, calling the count_spaces() function       
    print('Number of spaces: ', count_spaces(userInput))

    
# defining function that counts the number of spaces
# based on the user input
def count_spaces(userInput):
    spaces = 0
    for char in userInput:
        if char == " ":
            spaces = spaces + 1
    return spaces

mainFunction() # calling the main function
