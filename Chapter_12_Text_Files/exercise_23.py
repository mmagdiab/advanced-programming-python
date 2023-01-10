"""
An acronym is an abbreviation that uses the first letter of each word in a phrase. We see them
everywhere. For instance, NCAA for National Collegiate Athletic Association or NBC for
National Broadcasting Company. Write a program where the user enters an acronym and the
program randomly selects words from a wordlist such that the words would fit the acronym.
Below is some typical output generated when I ran the program:
Enter acronym: ABC
['addressed', 'better', 'common']
Enter acronym: BRIAN
['bank', 'regarding', 'intending', 'army', 'naive']
"""

words = ['addressed', 'better', 'common', 'bank', 'regarding', 'intending', 'army', 'naive']

result = []

acronym = input('Enter acronym:')

for c in acronym:
    for w in words:
        if w[0].lower() == c.lower():
            result.append(w)
            break

print(result)
