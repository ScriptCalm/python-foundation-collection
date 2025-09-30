
# Task 7.4

input_attempt = 1 # Set counter for no. of attempts
admin_password = 'changeme' # Set a password
user_password = str(input('Please enter your password: ')) # Input for password

while True: # Creating a loop
    if user_password == admin_password: # Check if the password is correct
        print('Password Accepted') # Message for password accepted
        print('You have done', input_attempt, 'attempt(s).') # Output the no.
        break

######### Condition added for limiting the maximum user tries to 5 attempts##############     
    else:
        if input_attempt == 5:
                print('You have done', input_attempt, 'wrong attempt(s).')
                print('Access denied. Please contact IT services to reset your password')
                break
#########################################################################################
            
        else:
            if user_password != admin_password: # Condition if password is incorrect
                input_attempt = input_attempt + 1 # Increment counter by 1
                user_password = str(input('Wrong password! Please try again: '))
                # output to try another password
                continue
