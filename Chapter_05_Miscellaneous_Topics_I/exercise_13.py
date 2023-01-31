from random import randint

wrong_count = 0
right_count = 0

for i in range(10):
    num_1 = randint(1,10)
    num_2 = randint(1,10)
    result = num_1 * num_2
    print('Question ', i+1, ': ', num_1, ' x ', num_2, ' = ', end='', sep='')
    guess = eval(input(''))
    if (guess == result):
        right_count += 1
        print('Right!') 
    else:
        wrong_count += 1
        print('Wrong!')
print(right_count, ' answers were right!')
print(wrong_count, ' asnwers were wrong!')