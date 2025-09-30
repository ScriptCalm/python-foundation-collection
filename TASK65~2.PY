
# Task 6.5.2

class invalidValue(Exception): # create custom error, derived from Exception class
    # error raised when the value < 0 or > 20
    # biggest earthquake ever recorded 9.5 Richter - 1960 Valdivia (wikipedia)
    pass

while True: # Creating a loop
    try:
        richterScale = float(input('Please enter the magnitude: ')) # input from user
        if richterScale < 0 or richterScale > 15: # check if the value inputted is valid
            raise invalidValue
    except (ValueError, invalidValue): # Catching the exceptions for invalid inputs
        print('You must enter a valid magnitude.') # Message for user if invalid input
        continue    
    if richterScale >= 8.0: # Creating a multi-way if-else statement block
        print('Most structures fall.')
        break
    else:
        if richterScale >= 7.0:
            print('Many buildings destroyed.')
            break
        else:
            if richterScale >= 6.0:
                print('Many buildings considerably damaged, some collapse.')
                break
            else:
                if richterScale >= 4.5:
                    print('Damage to poorly constructed buildings.')
                    break
                else:
                    if richterScale == 0: # Zero registered as no earthquake
                        print('No earthquake registered.')
                        break
                    else:
                        print('No destruction of buildings.')
                        break
                

   
    

