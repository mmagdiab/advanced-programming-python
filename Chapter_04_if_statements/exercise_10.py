from random import randint

for i in range(10):
    num_1 = randint(1,10)
    num_2 = randint(1,10)
    result = num_1 * num_2
    print('Question ', i+1, ': ', num_1, ' x ', num_2, ' = ', end='', sep='')
    guess = eval(input(''))
    if (guess == result):
        print('Right!')
    else:
        print('Wrong!') 