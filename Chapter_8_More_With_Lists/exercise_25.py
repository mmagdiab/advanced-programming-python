"""
Here is an old puzzle question you can solve with a computer program. There is only one
five-digit number n that is such that every one of the following ten numbers shares exactly
one digit in common in the same position as n. Find n.
01265, 12171, 23257, 34548, 45970, 56236, 67324, 78084, 89872, 99414
"""
from pprint import pprint

L = ['01265', '12171', '23257', '34548', '45970', '56236', '67324', '78084', '89872', '99414']
for i in range(10000, 100000):
    guess = str(i)
    flag = True
    for W in L:
        count = [guess[i] for i in range(5) if guess[i] == W[i]]
        if len(count) != 1:
            flag = False
            break
    if flag:
        print(i)
