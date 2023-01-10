"""
This problem is about a version of the game Jotto. The computer chooses a random five-letter
word with no repeat letters. The player gets several turns to try to guess the computer’s
word. On each turn, the player guesses a five-letter word and is told the number of letters
that their guess has in common with the computer’s word.
"""
from random import sample

alphabet = [chr(c) for c in range(65, 65+26)]

computer_word = ''.join(sample(alphabet, 5))

player_word = input('Enter your word:').upper()

while player_word.lower() != 'end':
    correct_letter = 0
    for c in computer_word:
        if c in player_word:
            correct_letter += 1
    player_word = input('Enter your word:').upper()

    print('Correct letter:', correct_letter)
