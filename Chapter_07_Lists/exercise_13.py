"""
Write a program that removes any repeated items from a list so that each item appears at most
once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].
"""
from random import sample
L = sample(range(0, 10), 7)
L += sample(range(0, 10), 7)
L += sample(range(0, 10), 7)
print(L)
for number in L:
    while L.count(number) > 1:
        first_occurrence = L.index(number)
        index = L[first_occurrence + 1:].index(number) + first_occurrence + 1
        del L[index]
print(L)
