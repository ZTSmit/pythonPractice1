from tkinter import *
from fibonacci_test import *


def fibby():
    fibGet = fibEntry.get()
    fibbyResult = fibonacci_check(fibGet)
    fibColor = 0
    fibColorInt = 0
    try:
        fibColor = int(fibGet)
    except ValueError:
        fibColor = 4090

    fibColorInt = fibColor      # This Block of code tries to convert the value given to a hexadecimal
    fibColor = hex(fibColor)    # number to make it applicable for changing the color of the label
    fibColor = str(fibColor)    # that the command creates
    fibColor = fibColor.replace("0x", "")
    if len(fibColor) > 3:               # The two if statements cut off the last digits or fill the first digits
        tempLength = len(fibColor) - 3  # with zeroes
        fibColor = fibColor[:-tempLength]
    if len(fibColor) < 3:
        tempLength = 3 - len(fibColor)
        while tempLength > 0:
            fibColor = "0" + fibColor
            tempLength -= 1

    fibColor = "#" + fibColor

    print(fibColor)  # Checks the color in console

    fibLabel.config(text=fibbyResult, bg=fibColor, foreground="#888")  # Modifies the placeholder label


root = Tk()

fibLabel = Label(root, text="Placeholder")
fibEntry = Entry(root, bg="#FFA")
myButton = Button(root, text="Click to check!", command=fibby, bg="#FFE")  # Placeholder values for the label

fibLabel.grid(row=1, column=2)
myButton.grid(row=99, column=2)
fibEntry.grid(row=1, column=1)

root.mainloop()
