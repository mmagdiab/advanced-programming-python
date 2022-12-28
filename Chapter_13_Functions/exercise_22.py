"""
A Tic-tac-toe board can be represented be a 3x3 two-dimensional list, where zeroes stand for
empty cells, ones stand for X’s and twos stand for O’s.
(a) Write a function that is given such a list and randomly chooses a spot in which to place
a 2. The spot chosen must currently be a 0 and a spot must be chosen.
(b) Write a function that is given such a list and checks to see if someone has won. Return
True if there is a winner and False otherwise.
"""
from random import randint

board_example = [[1, 0, 2],
                 [0, 2, 1],
                 [0, 0, 1]]


def a(board: list):
    row = randint(0, 2)
    colum = randint(0, 2)
    if board[row][colum] == 0:
        board[row][colum] = 2
    else:
        a(board)


def b(board: list):
    # Check for 3 1's in a row/colum or 3 2's in a row/colum
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return True
        if board[0][i] == board[1][i] == board[2][i]:
            return True
    # Check diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] == board[1][1] == board[2][0]:
        return True

    return False
