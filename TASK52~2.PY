
# Task 5.2.2

# Infant 0 years
# Child 1-14 years
# Teenager 15-19 years
# Adult > 20 years

from tkinter import * # import tkinter

root = Tk() # window
root.title('Age Stages') # window title

pls_enter = Label(root, text='Please enter your age:') # Tells what to do
pls_enter.grid(row=0, column=0, columnspan=3)

e = Entry(root, width=45, borderwidth=5) # input box
e.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

def button_click(number): # When click the button
    current = e.get() # what is in the box already
    e.delete(0, END) # delete what is in the box
    e.insert(0, str(current) + str(number)) # Insert numbers in correct order

def button_clear(): # Clear button action
    e.delete(0, END) # delete what is in the box

def button_enter(): # Enter button action
    age = int(e.get()) # What is in the box
    e.delete(0, END) # Clean the screen
    if age < 1:
        e.insert(0, 'You are an Infant.')
    elif age >= 1 and age <= 14:
        e.insert(0,'You are a Child.')
    elif age >=15 and age <=19:
        e.insert(0,'You are a Teenager.')
    else:
        e.insert(0,'You are an Adult.')
       
 # define buttons       
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_clear = Button(root, text='Clear', padx=30, pady=20, fg='red', command=button_clear)
button_enter = Button(root, text='Enter', padx=30, pady=20, fg='green', command=button_enter)
 # put buttons in grid
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0)
button_clear.grid(row=5, column=1)
button_enter.grid(row=5, column=2)

root.mainloop() # program's loop

