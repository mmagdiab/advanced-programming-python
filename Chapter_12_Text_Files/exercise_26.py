"""
Write a program to cheat at the game Scrabble. The user enters a string. Your program should
return a list of all the words that can be created from those seven letters.
"""
from itertools import permutations

word = input('Enter your word:')
print([''.join(p) for p in permutations(word)])
