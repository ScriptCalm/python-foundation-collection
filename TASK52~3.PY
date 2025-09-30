
# Task 5.2.3

# Infant 0 years
# Child 1-14 years
# Teenager 15-19 years
# Adult > 20 years

while True: # Creating a loop
    try: # Check if is valid input
        age = int(input("Please enter your age:")) # Take input from user
        if age < 0:
            # Raise error if input value is < 0
            raise ValueError('You have to enter a valid age.')
            continue
    except ValueError: # Error if input non integer
        print('You have to enter a valid age.')
        continue
# Multi-way 'if' statement
    if age == 0:
        print('You are an Infant.')
        break
    else:
        if age >=20:
            print('You are an Adult.')
            break
        else:
            if age >= 15:
                print('You are a Teenager.')
                break
            else:
                if age >= 1:
                    print('You are an Child')
                    break
                else:
                    print('You are an Infant.')
                    break
                
