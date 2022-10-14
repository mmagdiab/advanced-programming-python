width = eval(input('Enter the width: '))
height = eval(input('Enter the height: '))

print('*' * width)
for i in range(height-2):
    print('*', ' ' * (width-2), '*', sep='')
print('*' * width)