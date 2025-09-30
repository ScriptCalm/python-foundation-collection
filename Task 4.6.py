
# Task 4.6

from tkinter import* # Import tkinter module. (*) means import all tkinter packages.

root = Tk() # root creates the window widget (the main window of the program).
root.minsize(300, 300) # Sets a minimum size for the root to 300px by 300px.
root.title('My Program') # Sets a title for the program.
root.configure(background='black') # Set the background colour of the main window to black.

welcome = Label(root, text='Welcome to Python', bg='#ffcc00', fg='#003366').pack()
# Creates a welcome message with a defined background and foreground colour.

def atClick():  # Defines a function for when the button is clicked
        myLabel = Label(root, text='Thank you for clicking me!', fg='#fff799', bg='#000099')
        # This line creates (defines) a label widget inside the main window (root)
        
        myLabel.pack() # this line makes the label to be displayed on the screen

myButton = Button(root, text='Click here', command=atClick, fg='#fff799', bg='#a0410d')
# Defines a button widget using Button() function, inside the root (main window),
# set a text to be shown on the button,
# and we assign a function to be executed when clicked (command=...).
        # When assigned, the function doesn't need the pair of brackets ().
# fg='#fff799'(foreground colour) sets the colour of the text on the button to a specified colour code.
# bg='#a0410d' (background colour) sets the background colour of the button to a specified colour code.
# colours can be picked from https://www.w3schools.com/colors/colors_picker.asp or other sources.

myButton.pack() # Displays the button on the screen

root.mainloop() # this line creates the main loop of the program,
                # called the event loop, which registers all the changes at any point
