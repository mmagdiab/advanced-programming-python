"""
Write a program in Python that displays a window to the user that asks them to enter an
integer N and displays its factorial N !
"""
from tkinter import *


def callback():
    n = eval(entry_input.get())
    if n < 0:
        label_result.configure(text='Cannot process negative values.')
        return
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    label_result.configure(text='The factorial of ' + str(n) + ' is ' + str(n) + '! ' + '= ' + str(factorial))

root = Tk()

screen_font = ('arial', 12)

label_1 = Label(text='Enter value of integer N :', font=screen_font)
label_result = Label(font=screen_font)

entry_input = Entry(font=screen_font, width=20)
button_validate = Button(text='Validate', font=screen_font, width=20, command=callback)

# Let's grid out widgets
label_1.grid(row=0, column=0, padx=10, pady=10)
entry_input.grid(row=0, column=1, padx=10, pady=10)
label_result.grid(row=1, column=1)
button_validate.grid(row=2, column=1, padx=10, pady=10)

mainloop()


