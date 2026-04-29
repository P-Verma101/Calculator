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

def button_clicked(symbol):
    """
    This is a function that handles the button clicks for the
    calculator. The arguement 'symbol' refers to the button that
    is being clicked.
    The  line "global calculator" is used to make the 'calculator'
    variable accessible and modifiable anywhere within the code.
    The 'calculator += str(symbol)' line appends the button to
    the calculation.
    The 'text_result.delete(1.0, "end")' line clears the 
    current text in the display.
    The 'text_result.insert(1.0, calculator)' line updates the
    display with the new calculation.
    """
    global calculator # --> Shares memory
    calculator += str(symbol) # --> Builds equation
    text_result.delete(1.0, "end") #--> Fresh screen
    text_result.insert(1.0, calculator) # --> Shows result


def evaluate_calculator():
    """
    This function calculates the result of the equation. This
    is the function for the 'equals' button.
    The first line of code in this function is the same as the 
    last function.
    The 'try' block that is used in this function is used for 
    error protection. 
    Inside the 'try' block, the 'calculator = str(eval(calculator))'
    line evaluates the expression in the 'calculator' variable
    and coverts the result back to a string.
    The 'text_result.delete(1.0, "end ")' and the 
    'text_result.insert(1.0, calculator)' lines are the same as
    in the last function; they clear the display and show the
    result.
    The 'except' block is executed if there is catches the errors
    that may occur during an equation evaluation. If an error
    occurs, the 'clear_calculator()' function is called to reset
    the calculator, and the display is updated to show "Error".
    """
    global calculator
    try:
        calculator =  str(eval(calculator))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculator)
    except:
        clear_calculator()
        text_result.insert(1.0, "Error")


def clear_calculator():
    """
    This function clears the calculator.
    """
    global calculator
    calculator = ""
    text_result.delete(1.0, "end")


"""
This line of code create the Main application window. 'tk.Tk()'
creates a new empty window ("the root window"). 'root' is the
variable that holds a reference to this window. If this line
is run by itself, it will create an empty window.
"""
root = tk.Tk()

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
This line of code createa  blig 2-line text area.
This is the calculcator screen.
"""
text_result = tk.Text(root, height = 2, width = 16, font = ("Arial", 24))
"""
This puts the display at the top of of a 5-column
grid, spanning all 5 columns. This allows the display
to be centered and take up the full width of the
calculator. The grid system is a way to organize
the layout of the GUI elements in a structured way.
"""
text_result.grid(columnspan = 5)

"""
The lines of code below create the buttons for the calculator.
The first loop creates the number buttons (1-9) and arranges 
them in a 3x3 grid. The second loop creates the operation buttons
(+, -, *, /) and arranges them in a single column. The last two
lines create the 'equals' and 'clear' buttons and position them
appropriately on the grid. Each button is associated with a 
command that specifies what happens when the button is clicked. 
For example, when a number button is clicked, it calls the 
'button_clicked' function with the corresponding number as an 
argument. When the 'equals' button is clicked, it calls the 
'evaluate_calculator' function to compute the result.
"""
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for i, num in enumerate(numbers):
    row = 2 + (i // 3)
    col = 1 + (i % 3)
    tk.Button(root, text = num, command = lambda n=num: button_clicked(n), width = 5, font = ("Arial", 14)).grid(row = row, column = col)

tk.Button(root, text = '0', command = lambda: button_clicked('0'), width = 5, font = ("Arial", 14)).grid(row = 5, column = 2)

operations = ['+', '-', '*', '/']
for i, op in enumerate(operations):
    tk.Button(root, text = op, command = lambda o=op: button_clicked(o), width = 5, font = ("Arial", 14)).grid(row = 2 + i, column = 4)

tk.Button(root, text = '=', command = evaluate_calculator, width = 5, font = ("Arial", 14)).grid(row = 5, column = 3)
tk.Button(root, text = 'CLR', command = clear_calculator, width = 5, font = ("Arial", 14)).grid(row = 5, column = 1)

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
