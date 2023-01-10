"""
In a magic square, each row, each column, and both diagonals add up to the same number.
A partially filled magic square is shown below. Write a program to check through all the
possibilities to fill in the magic square.
5 _ _
_ 6 2
3 8 _
"""


def is_magic(square):
    _sum = sum(square[0])
    # Check rows
    for row in square:
        if sum(row) != _sum:
            return False
    # Check column
    if (square[0][0] + square[1][0] + square[2][0]) != \
            (square[0][1] + square[1][1] + square[2][1]) != \
            (square[0][2] + square[1][2] + square[2][2]) != _sum:
        return False

    # Check diagonals
    if (square[0][0] + square[1][1] + square[2][2]) != \
            (square[2][0] + square[1][1] + square[0][2]) != _sum:
        return False

    return True


example = [[5, 0, 0],
           [0, 6, 2],
           [3, 8, 0]]

spots = [[i, j] for i in range(len(example)) for j in range(len(example[0])) if example[i][j] == 0]

for i in range(10):
    example[spots[0][0]][spots[0][1]] = i
    for j in range(10):
        example[spots[1][0]][spots[1][1]] = j
        for k in range(10):
            example[spots[2][0]][spots[2][1]] = k
            for m in range(10):
                example[spots[3][0]][spots[3][1]] = m
                if is_magic(example):
                    print(example)
