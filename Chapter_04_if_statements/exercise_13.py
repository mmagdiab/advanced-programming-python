from random import randint

# Rock -> 1
# Paper -> 2
# Scissors -> 3

computer_score = 0
player_score = 0

for i in range(5):
    print('Round [', i+1, '] Choose rock (1), paper(2), scissors(3): ', sep='', end='')
    P_selection = eval(input(''))
    C_selection = randint(1,3)
    if (C_selection == 1):
        print('Computer selects rock.')
    elif (C_selection == 2):
        print('Computer selects papers.')
    else:
        print('Computer selects scissors.')
    if (P_selection == C_selection):
        print('Tie.')
    elif ((P_selection == 1 and C_selection == 3) or P_selection > C_selection):
        print('You beat computer')
        player_score += 1
    else:
        print('Ouch!')
        computer_score += 1

if (player_score > computer_score):
    print('You win!')
elif (player_score < computer_score):
    print('Computer wins!')
else:
    print('Tie!')