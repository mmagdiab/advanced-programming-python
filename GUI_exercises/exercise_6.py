"""
Create a Python program using the Tkinter library, which displays a dialog box that ask user to
type his name and display a dialog box asking him to enter his name and displays the welcome
message followed by his name.
"""
from tkinter import *


def callback():
    name = entry_input.get()
    label_result.configure(text='Welcome ' + name + ' !')


root = Tk()

screen_font = ('arial', 12)

label_1 = Label(text='Enter your name :', font=screen_font)
label_result = Label(font=screen_font)

entry_input = Entry(font=screen_font, width=20)
button_validate = Button(text='Validate', font=screen_font, width=20, command=callback)

# Let's grid out widgets
label_1.grid(row=0, column=0, padx=10, pady=10)
entry_input.grid(row=0, column=1, padx=10, pady=10)
button_validate.grid(row=1, column=1)
label_result.grid(row=2, column=1, padx=10, pady=10)

mainloop()
