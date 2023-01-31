input = eval(input('Enter a number: '))
for i in range (2, input):
    if (input % i == 0):
        print(i)