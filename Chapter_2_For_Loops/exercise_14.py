height = eval(input('Enter the height: '))
height = (height-1+2)//2

for i in range(height):
    print(' ' * (height - 1 	- i), end='')
    print('*' * (i * 2 + 1))

for i in range(height):
    print(' ' * (i + 1), end='')
    print('*' * ((height-1-i) * 2  - 1))