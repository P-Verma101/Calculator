"""
#The line below is used to import the tkinter library, which is 
# a standard GUI (Graphical User Interface) toolkit in Python. 
# It allows you to create windows, buttons, labels, and other 
# GUI elements for your application. By importing tkinter, you 
# can use its functions and classes to build a simple calculator
# interface.
"""
import tkinter as tk 

"""
This line of code initializes and empty line of code that will
be used to keep track of all the numbers that are inputed into
the calculator. This is a string variable that will be updated
as the user inputs/interacts with the calculator.
"""
calculator= ""

def add_to_calculator(symbol):
    pass

def evaluate_calculator():
    pass

def clear_calculator():
    pass

"""
This line of code create the Main application window. 'tk.Tk()'
creates a new empty window ("the root window"). 'root' is the
variable that holds a reference to this window. If this line
is run by itself, it will create an empty window.
"""
root = tk.Tk()

"""
This line of code starts the GUI event loop. This keeps the
window open and responsive. Without this line, the window would
open and then close right away. This line essentially listens
to the users interactions with the GUI such as the mouse clicks,
keyboard input, etc. This updates the display in accordance to 
the users interactions. This keeps apps running until the user
closes the window or exits the application.
"""
root.mainloop()

"""
This line of code sets the size of the main application window
that was created with the line root = tk.Tk(). The 'geometry'
method is used to simplify the process of setting the size of 
the window. The string "300x400" specifies the width and height
of the the window in pixels. In this case, the window will be 
300 pixels wide and 400 pixels tall. 
"""
root.geometry("300x400")
"""
This line of code sets 
"""
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))