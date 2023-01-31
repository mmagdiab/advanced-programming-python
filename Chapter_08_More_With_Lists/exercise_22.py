"""
The following is useful as part of a program to play Battleship. Suppose you have a 5  5 list
that consists of zeroes and ones. Ask the user to enter a row and a column. If the entry in the
list at that row and column is a one, the program should print Hit and otherwise it should
print Miss.
"""
from random import randint
from pprint import pprint

L = [[randint(0, 1) for i in range(5)] for j in range(5)]
pprint(L)

row = eval(input('Enter a row: ')) + 1
column = eval(input('Enter a column: ')) + 1
if L[row][column] == 1:
    print('Hit')
else:
    print('Miss')
