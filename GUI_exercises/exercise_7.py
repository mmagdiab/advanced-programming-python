"""
Using the Tkinter Python library, write a Python program that displays a dialog box asking the
user to enter an integer and return its double
"""
from tkinter import *


def callback():
    n = eval(entry_1.get())
    entry_2.delete(0, END)
    entry_2.insert(0, n*2)


root = Tk()

screen_font = ('arial', 12)

label_1 = Label(text='Enter value of integer N', font=screen_font)
label_2 = Label(text='Here is the double 2*N:', font=screen_font)

entry_1 = Entry(font=screen_font, width=20)
entry_2 = Entry(font=screen_font, width=20)
button_validate = Button(text='Validate', font=screen_font, width=20, command=callback)

# Let's grid out widgets
label_1.grid(row=0, column=0, padx=10, pady=10)
label_2.grid(row=1, column=0, padx=10, pady=10)
entry_1.grid(row=0, column=1, padx=10, pady=10)
entry_2.grid(row=1, column=1, padx=10, pady=10)

button_validate.grid(row=3, column=1, padx=10, pady=10)

mainloop()