"""
Create a graphical application in Python Tkinter that asks the user to enter an integer N and
displays them the value of the sum "1 + 2 + ... + N"
"""
from tkinter import *


def callback():
    n = eval(entry_input.get())
    result = sum([i for i in range(1, n+1)])
    if n > 2:
        label_result.configure(text='The sum is 1 + 2 + .. + ' + str(n) + ' = ' + str(result))
    else:
        label_result.configure(text='The sum is ' + ' = ' + str(result))


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

