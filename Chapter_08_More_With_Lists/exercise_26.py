"""
We usually refer to the entries of a two-dimensional list by their row and column, like below
on the left. Another way is shown below on the right.
(0,0) (0,1) (0,2) 0 1 2
(1,0) (1,1) (1,2) 3 4 5
(2,0) (2,1) (2,2) 6 7 8
(a) Write some code that translates from the left representation to the right one. The // and
% operators will be useful. Be sure your code works for arrays of any size.
(b) Write some code that translates from the right representation to the left one.
"""


def a():
    rows, columns = eval(input('Enter list dimensions: '))
    row, column = eval(input('Enter element coordinates: '))
    result = (row * columns) + column
    return result


def b():
    rows, columns = eval(input('Enter list dimensions: '))
    sequence = eval(input('Enter element sequence: '))
    row = sequence // columns
    column = sequence % columns
    return '(' + str(row) + ', ' + str(column) + ')'


