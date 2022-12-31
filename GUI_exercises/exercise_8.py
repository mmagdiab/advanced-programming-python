"""
Create a program in Python that which a Tkinter window asking the user to enter an integer N
and returns all the divisors of N.
"""

from tkinter import *


def callback():
    n = eval(entry_1.get())
    divisors = [str(i) for i in range(1, n+1) if n % i == 0]
    result_message = "    ".join(divisors)
    label_result.configure(text=result_message)


root = Tk()

screen_font = ('arial', 12)

label_1 = Label(text='Enter value of integer N :', font=screen_font)

label_2 = Label(font=screen_font, text='The divisors of N :')
label_result = Label(font=screen_font)

entry_1 = Entry(font=screen_font, width=20)
button_validate = Button(text='Validate', font=screen_font, width=20, command=callback)

# Let's grid out widgets
label_1.grid(row=0, column=0, padx=10, pady=10)
entry_1.grid(row=0, column=1, padx=10, pady=10)
label_2.grid(row=1, column=0)
label_result.grid(row=1, column=1)
button_validate.grid(row=3, column=1, padx=10, pady=10)

mainloop()
