"""
(a) Write a program that converts Roman numerals into ordinary numbers. Here are the
conversions: M=1000, D=500, C=100, L=50, X=10, V=5 I=1. Don’t forget about things
like IV being 4 and XL being 40.
(b) Write a program that converts ordinary numbers into Roman numerals
"""
# for simplicity, I will work on only first 5 number
d = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}


def a(roman_numerals):
    print(d[roman_numerals])


def b(ordinary_number):
    for i in d:
        if d[i] == ordinary_number:
            print(i)
            break
