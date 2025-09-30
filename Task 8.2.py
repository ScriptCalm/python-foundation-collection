
# Task 8.2

def main(): # Defining first function
    a = 5 # variable used as parameters in mystery function
    b = 7 # variable used as parameters in mystery function
    print(mystery(a, b)) # Calling the second function (mystery)
                         # inside of a print statement
                         
def mystery(x, y): # Defining the second function
    z = x + y # first mathematical operation
    z = z / 2.0 # second mathematical operation
                # using the result from the first operation
    return z # returning the result

main() # Calling the first function which is printing the result

