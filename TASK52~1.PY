
# Task 5.2.1

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
# if - elif - else control structure for checking age brackets
    if age == 0:
        print('You are an Infant.')
        break
    elif age >= 1 and age <= 14:
        print('You are a Child.')
        break
    elif age >=15 and age <=19:
        print('You are a Teenager.')
        break
    else:
        print('You are an Adult.')
        break
