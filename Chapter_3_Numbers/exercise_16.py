from math import floor
Y = eval(input('Enter a year: '))
C = (Y / 100) + 1

m = (15 + C - floor(C/4) - floor((8*C+13)/25)) % 30
n = (4 + C - floor(C/4)) % 7
a = Y % 4
b = Y % 7
c = Y % 19
d = (19*c + m) % 30
e = (2*a + 4*b + 6*d + n) % 7 

march = 22 + d + e
april = d + e - 9

list = [2, 5, 10, 13, 16, 21, 24, 39]

if d == 29 and e == 6:
    print('Exception: Easter is on April 18')
elif d == 28 and e == 6 and m in list:
    print('Exception: Easter is on April 19')
else:
    print('Easter is in March ', march)
    print('Or in April ', april)