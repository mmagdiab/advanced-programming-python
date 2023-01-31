from random import randint

user_score = 0

for i in range(5):
    number_to_guess = randint(1,10)
    user_guess = eval(input('Enter your guess between 1 and 10: '))
    if (number_to_guess == user_guess):
        user_score += 10
        print('Good job!')
    else:
        user_score = max(0, user_score - 1)
        print('Wrong guess.')

print('Your score is: ', user_score)		