"""
Write a program that asks the user to enter a length in feet. The program should then give
the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
enter a 2, then the program converts to yards, etc. While this can be done with if statements,
it is much shorter with lists and it is also easier to add new conversions if you use lists.
"""
length = eval(input("Enter length in feet:"))
length_converted = [length, length*12, length/3, length/5280, length*304.8,
                    length*30.48, length/3.281, length/3281]
code = eval(input("Enter 1 for inches, 2 for yards...:"))
print(length_converted[code])
