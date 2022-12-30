"""
Write a program that asks the user to type a word and return him its reverse without using
any predefined function. Example if the user enters the word python, the program returns
nohtyp to him.
"""
from tkinter import *


def callback():
    user_input = entry_input.get()
    label_result.configure(text=user_input[::-1])


root = Tk()

screen_font = ('arial', 12)

label_1 = Label(text='Enter a word :', font=screen_font)
label_result = Label(font=screen_font)

entry_input = Entry(font=screen_font, width=20)
button_validate = Button(text='Validate', font=screen_font, width=20, command=callback)

# Let's grid out widgets
label_1.grid(row=0, column=0, padx=10, pady=10)
entry_input.grid(row=0, column=1, padx=10, pady=10)
label_result.grid(row=1, column=1)
button_validate.grid(row=2, column=1, padx=10, pady=10)

mainloop()
