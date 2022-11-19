"""
Write a program that generates 100 random integers that are either 0 or 1. Then find the
longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.
"""
from random import randint
L = []
for i in range(100):
    L.append(randint(0, 1))
longest_run = 0
current_run = 0
for number in L:
    if number == 0:
        current_run += 1
    else:
        current_run = 0
    if current_run > longest_run:
        longest_run = current_run
print(longest_run)
