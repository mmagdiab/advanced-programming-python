"""
Create a graphical application with Python Tkinter which tests whether a given integer is a
perfect square or not.
"""
from tkinter import *


def callback():
    # The Square root at least is small then (the half value of n)
    n = eval(entry_input.get())
    result = -1
    for i in range(1, (n//2) + 1):
        if i * i == n:
            result = i
            break
    if result == -1:  # if not found
        label_result.configure(text='Input is not a perfect square')
    else:
        label_result.configure(text=str(n) + ' is a perfect square ' + str(n) + ' = ' + str(i) + ' ^  2')


root = Tk()

screen_font = ('arial', 12)

label_1 = Label(text='Enter value of integer N :', font=screen_font)
label_result = Label(font=screen_font)

entry_input = Entry(font=screen_font, width=20)
button_validate = Button(text='Validate', font=screen_font, width=20, command=callback)

# Let's grid out widgets
label_1.grid(row=0, column=0, padx=10, pady=10)
entry_input.grid(row=0, column=1, padx=10, pady=10)
button_validate.grid(row=1, column=1)
label_result.grid(row=2, column=1, padx=10, pady=10)

mainloop()
