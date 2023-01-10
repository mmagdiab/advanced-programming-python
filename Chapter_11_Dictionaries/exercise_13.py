"""
Suppose you are given the following list of strings:
L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']
Patterns like this show up in many places, including DNA sequencing. The user has a
string of their own with only some letters filled in and the rest as asterisks. An example
is a**a****. The user would like to know which of the strings in the list fit with their pattern.
In the example just given, the matching strings are the first and fourth. One way to
solve this problem is to create a dictionary whose keys are the indices in the user’s string of
the non-asterisk characters and whose values are those characters. Write a program implementing
this approach (or some other approach) to find the strings that match a user-entered
string.
"""
L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']

patterns = [{i: pattern[i] for i in range(len(pattern))} for pattern in L]

user_dna = input('Enter your dna:')

dna = {i: user_dna[i] for i in range(len(user_dna))}

for pattern in patterns:
    matched = True
    for c in dna:
        if dna[c] != '*' and dna[c] != pattern[c]:
            matched = False
            break

    if matched:
        print(pattern)
