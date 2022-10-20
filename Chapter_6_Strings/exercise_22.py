from math import ceil


def part_a():
    # Encrypt
    message = input('Enter the secret message: ')
    encrypted_message = message[0::2]
    encrypted_message += message[1::2]
    print(encrypted_message)


def part_b():
    # Decrypt
    encrypted_message = input('Enter the encrypted message: ')
    message_length = len(encrypted_message)
    decrypted_message = ''
    for i in range(message_length//2):
        decrypted_message += encrypted_message[i] + encrypted_message[i+ceil(message_length/2)]
    if len(decrypted_message) < len(encrypted_message):
        decrypted_message += encrypted_message[message_length // 2]
    print(decrypted_message)
