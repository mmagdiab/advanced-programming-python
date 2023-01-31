height = eval(input('Enter the height: '))

for i in range(height):
    print(' ' * (height-i-1), end='')
    print('*', end='')
    if i == height//2:
        print('*' * (i*2-1), end='')
    else:
        print(' ' * (i*2-1), end='')
    if i > 0:
        print('*')
    else:
        print()	