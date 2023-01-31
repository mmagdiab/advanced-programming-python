"""
The following is useful in implementing computer players in a number of different games.
Write a program that creates a 5 x 5 list consisting of zeroes and ones. Your program should
then pick a random location in the list that contains a zero and change it to a one. If all the
entries are one, the program should say so. [Hint: one way to do this is to create a new list
whose items are the coordinates of all the ones in the list and use the choice method to
randomly select one. Use a two-element list to represent a set of coordinates.]
"""
from pprint import pprint
from random import randint, choice

L = [[randint(0, 1) for i in range(5)] for j in range(5)]
coordinates = [[x, y] for x in range(5) for y in range(5) if L[x][y] == 0]
pprint(L)
for coordinate in coordinates:
    L[coordinate[0]][coordinate[1]] = 1
    pprint(L)
