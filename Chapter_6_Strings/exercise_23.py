from math import ceil


def part_a():
    message = input('Enter a message: ')
    encrypted_message = message[::3] + message[1::3] + message[2::3]
    print(encrypted_message)


def part_b():
    encrypted_message = input('Enter encrypted message: ')
    decrypted_message = ''
    part_length = ceil(len(encrypted_message)/3)
    for i in range(part_length):
        decrypted_message += encrypted_message[i]
        if i + part_length < len(encrypted_message):
            decrypted_message += encrypted_message[i+part_length]
        if i + part_length*2 < len(encrypted_message):
            decrypted_message += encrypted_message[i+(part_length*2)]
    print(decrypted_message)


def part_c():
    message = input('Enter a message: ')
    section_size = eval(input('Please input break size: '))
    encrypted_message = ''
    for i in range(section_size):
        encrypted_message += message[i::section_size]
    print(encrypted_message)


def part_d():
    encrypted_message = input('Enter encrypted message: ')
    section_size = eval(input('Please input break size: '))
    decrypted_message = ''
    part_length = ceil(len(encrypted_message)/section_size)
    for i in range(part_length):
        decrypted_message += encrypted_message[i]
        for j in range(1, part_length+1):
            if i + part_length*j < len(encrypted_message):
                decrypted_message += encrypted_message[i+(part_length*j)]
    print(decrypted_message)


part_c()
