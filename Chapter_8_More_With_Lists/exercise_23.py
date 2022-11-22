"""
This exercise is useful in creating a Memory game. Randomly generate a 6 x 6 list of assorted
characters such that there are exactly two of each character. An example is shown below.
@ 5 # A A !
5 0 b @ $ z
$ N x ! N z
0 - + # b :
- : + c c x
"""
from pprint import pprint
from string import punctuation, ascii_lowercase
from random import sample, shuffle
pool = punctuation + ascii_lowercase

L = sample(pool, 18) * 2
shuffle(L)
L = [[L[i] for i in range(j, j+6)] for j in range(0, 36, 6)]
pprint(L)
