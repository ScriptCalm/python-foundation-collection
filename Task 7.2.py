
# Task 7.2.1

number = 0 # Starting point 0
while number <=14: # Loop ends at 14 (15 loops total, 0-14)
    number = number + 1 # First incrementation outputting 1   
    if number == 3: # Condition for skipping no.3
        # Just skipping without any output
        continue
    elif number == 5: # Condition for skipping no. 5
        print('Skipping 5')
        continue
    else:
        if number == 7: # Condition for skipping no. 7
            print('Skipping 7')
            continue
    print(number) # Outputting the number after incrementation
