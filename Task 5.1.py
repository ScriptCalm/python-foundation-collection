
# Task 5.1

print('Input area.')
p = str(input('p = Please enter your first name: '))  
q = str(input('q = Please enter your sur name: '))  
r = str(input('r = Please enter any word: ')) 

print(' ') # Space
print('Output area:')

# Concatenation (p+q+r) in capital letters
print('p+q+r in capital letters: ', p.upper() + q.upper() + r.upper())

# Concatenation of (r + p) in lowercase
print('r + p in lowercase: ', r.lower()+ ' ' + p.lower())

# total number of characters within (p+q+r)
print('Total no. of characters (p+q+r): ',len(p + q + r)) 
