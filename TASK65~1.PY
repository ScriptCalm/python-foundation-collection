
# Task 6.5.1

richterScale = float(input('Please enter the magnitude: ')) # user input

if richterScale >= 8.0: # First condition
    print('Most structures fall.')
elif richterScale >= 7.0 and richterScale < 8.0: # Second condition
    print('Many buildings destroyed.')
elif richterScale >= 6.0 and richterScale <7.0: # Third condition
    print('Many buildings considerably damaged, some collapse.')
elif richterScale >= 4.5 and richterScale <6.0: # Fourth condition
    print('Damage to poorly constructed buildings.')
else: # executed if non of the conditions were met
    print('No destruction of buildings.')


   
    

