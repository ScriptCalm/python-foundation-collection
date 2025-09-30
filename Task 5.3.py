
# Task 5.3

# underweight < 18.5 BMI
# healthy weight 18.5 - 24.9 BMI
# overweight > 25.0 BMI

# function definition for testing the weight input
def tryWeight(text): 
    while True: # Open a while loop for try block
        try:
            number = float(input(text)) # takes the input from user         
            if number < 0.5 or number > 450 : # check the value validity
                print('You must enter a valid value of the weight in kgs.')
            else:
                return number # Keeps the value as a float, not as a boolean
                break
        except ValueError: # Error if is not a numerical input
            print('You must enter a numerical value (weight in kgs).')

            
# function definition for testing the height input
def tryHeight(text): 
    while True: # Open a while loop for try block
        try:
            number = float(input(text)) # takes the input from user 
            if number < 0.3 or number > 2.8 : # check the value validity
                print('You must enter a valid value of the height in meters.')
            else:
                return number # Keeps the value as a float, not as a boolean
                break           
        except ValueError: # Error if is not a numerical input
            print('You must enter a numerical value (height in meters).')

# define variables based on the try functions above
weight = tryWeight('Please enter your weight in kgs: ')
height = tryHeight('Please enter your height in meters: ')

print(' ')    # Space
bmi = float(round(weight /(height ** 2), 2)) # Calculates BMI
print('Your BMI is: ', bmi) # Print BMI

# Control statements for underweight, healthy weight or overweight 
if bmi < 18.5:
    print('You are underweight')

elif bmi >= 18.5 and bmi <=24.9:
    print('You have a healthy weight')

else:
    print('You are overweight')

