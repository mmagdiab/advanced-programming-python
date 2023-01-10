"""
The following is useful as part of a program to play Minesweeper. Suppose you have a 5 x 5
list that consists of zeros andM’s. Write a program that creates a new 5x5 list that hasM’s in
the same place, but the zeroes are replaced by counts of how many M’s are in adjacent cells
(adjacent either horizontally, vertically, or diagonally). An example is shown below. [Hint:
short-circuiting may be helpful for avoiding index-out-of-range errors.]
0 M 0 M 0   1 M 3 M 1
0 0 M 0 0   1 2 M 2 1
0 0 0 0 0   2 3 2 1 0
M M 0 0 0   M M 2 1 1
0 0 0 M 0   2 2 2 M 1
"""
from pprint import pprint


def adjacent_m_sum(row, column, board):
    _sum = 0
    if row > 0:
        if board[row-1][column] == 'M':
            _sum += 1
    if row < len(board) - 1:
        if board[row+1][column] == 'M':
            _sum += 1
    if column > 0:
        if board[row][column-1] == 'M':
            _sum += 1
    if column < len(board[0]) - 1:
        if board[row][column+1] == 'M':
            _sum += 1

    return _sum


example = [['0', '0', 'M',  '0',  'M',  '0'],
           ['0', 'M', '0',  'M',  'M',  '0']]

for i in range(len(example)):
    for j in range(len(example[i])):
        if example[i][j] == '0':
            example[i][j] = adjacent_m_sum(i, j, example)

pprint(example)
