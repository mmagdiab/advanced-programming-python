from random import randint

PLAY_TIMES = 10000


def play(size):
    # Randomly generate prize, user guess location
    prize_location = randint(1, size)
    user_guess = randint(1, size)
    if user_guess == prize_location:
        return True
    else:
        return False


def part_a():
    keep_count = 0
    switch_count = 0
    for i in range(PLAY_TIMES):
        result = play(3)
        if result:
            keep_count += 1

    switch_count = PLAY_TIMES - keep_count
    print('Keep win percentage: ', round((keep_count/PLAY_TIMES) * 100, 2), '%', sep='')
    print('Switch win percentage: ', round((switch_count/PLAY_TIMES) * 100, 2), '%', sep='')


def part_b():
    keep_count = 0
    switch_count = 0
    for i in range(PLAY_TIMES):
        result = play(4)
        if result:
            keep_count += 1

    switch_count = PLAY_TIMES - keep_count
    print('Keep win percentage: ', round((keep_count / PLAY_TIMES) * 100, 2), '%', sep='')
    print('Switch win percentage: ', round((switch_count / PLAY_TIMES) * 100, 2), '%', sep='')

