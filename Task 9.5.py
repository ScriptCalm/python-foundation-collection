
# Task 9.5

class gregorianCalendar(Exception): # exception to check if above 1582
    pass

while True: # check for validity input
    try:
        year = int(input('Please enter an year: '))
        if year <= 1582:
            raise gregorianCalendar
        
    except gregorianCalendar: # check if gregorian calendar
        print('Year must be greater than 1582 - the first year of Gregorian calendar.')
        continue
    except ValueError: # if not numerical input
        print('You must enter a valid year (numerical).')
        continue
    else:
        break


def checkYear(y): # function for checking if leap year or not
    if ( y%4==0 and y%100!=0 ) or ( y%400 == 0 ):
        print(f'{y} is a leap year.')
    else:
        print(f'{y} is not leap year.')
 
checkYear(year) # calling the function
