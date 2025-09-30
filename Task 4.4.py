
# Task 4.4

import calendar # Importing calendar module

print('Input area')

# Input for year
year = int(input("Please enter the year in format YYYY: "))

# Input for month
month = int(input("Please enter the month in format MM: "))

print(' ') # Space
print('Output area:')

# Print the calendar for the year and month inputted
print(calendar.month(year, month))
