
# Task 4.5

# define a function called interestCalculator with current ballance and
# yearly interes as parameters
def interestCalculator(currentBallance, year_interest):
    
    # defining variable with mathematical formulas for each year
    year_1 = currentBallance + ((currentBallance * year_interest)/100)
    year_2 = year_1 + ((year_1 * year_interest)/100)
    year_3 = year_2 + ((year_2 * year_interest)/100)
    year_4 = year_3 + ((year_3 * year_interest)/100)

    # print statements for each year
    print('First Year Ballance is: ', round(year_1, 2))
    print('Second Year Ballance is: ', round(year_2, 2))
    print('Third Year Ballance is: ', round(year_3, 2))
    print('Fourth Year Ballance is: ', round(year_4, 2))

# calling the function with user input for current ballance parameter
interestCalculator(float(input('Please enter your current ballance: ')), 5)











