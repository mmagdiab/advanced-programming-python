"""
Create a Tkinter GUI interface, which calculates the greatest common divisor GCD and the
least common multiple LCM graphically.
"""
from tkinter import *
from tkinter import ttk


def callback(event):
    m = eval(entry_1.get())
    n = eval(entry_2.get())
    # Naive solution
    if choice.get() == 'GCD':
        gcd = 1
        for i in range(2, min(m, n)+1):
            if m % i == 0 and m % i == 0:
                gcd = i
        label_result.configure(text="GCD(m, n) = " + str(gcd))
    elif choice.get() == 'LCM':
        lcm = -1
        for i in range(max(m, n), m*n + 1):
            if i % m == 0 and i % m == 0:
                lcm = i
                break
        label_result.configure(text="LCM(m, n) = " + str(lcm))


root = Tk()

screen_font = ('arial', 12)

label_1 = Label(text='Enter value of m :', font=screen_font)
label_2 = Label(text='Enter value of n :', font=screen_font)
label_3 = Label(text='Choose function:', font=screen_font)

choice = StringVar()
choice.set('- SELECT -')

combobox = ttk.Combobox(font=screen_font, textvariable=choice, values=['GCD', 'LCM'], width=18)
combobox.bind('<<ComboboxSelected>>', callback)

label_result = Label(font=screen_font)

entry_1 = Entry(font=screen_font, width=20)
entry_2 = Entry(font=screen_font, width=20)

# Let's grid out widgets
label_1.grid(row=0, column=0, padx=10, pady=10)
label_2.grid(row=1, column=0, padx=10, pady=10)
label_3.grid(row=2, column=0, padx=10, pady=10)

entry_1.grid(row=0, column=1, padx=10, pady=10)
entry_2.grid(row=1, column=1, padx=10, pady=10)

combobox.grid(row=2, column=1, padx=10, pady=10)

label_result.grid(row=3, column=1, padx=10, pady=10)

mainloop()
