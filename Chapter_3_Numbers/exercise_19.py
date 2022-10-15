width = eval(input('Enter the width: '))
height = eval(input('Enter the height: '))

counter = 0

for i in range(height):
    for i in range(width):
        if counter == 10:
            counter = 0
        print(counter, end=' ')
        counter += 1
    print()