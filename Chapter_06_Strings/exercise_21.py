from random import randint

string = input('Enter a word: ')
new_string = ''
for i in range(len(string)):
    random_index = randint(0, len(string)-1)
    new_string += string[random_index]
    string = string[:random_index] + string[random_index+1:]

print('The new arrangement: ', new_string)
