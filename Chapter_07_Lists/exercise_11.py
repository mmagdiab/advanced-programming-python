"""
Using a for loop, create the list below, which consists of ones separated by increasingly many
zeroes. The last two ones in the list should be separated by ten zeroes.
[1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]
"""
L = []
for i in range(10):
    L += [1]
    L += [0] * i
L += [1]
print(L)
