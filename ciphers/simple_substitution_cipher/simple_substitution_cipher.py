import string
import random

alphabet = string.ascii_uppercase + ' '
key = alphabet
m = 26 + 1


def generate_key():
    cipher_alphabet = alphabet[:-1]
    cipher_alphabet = ''.join(random.sample(cipher_alphabet, len(cipher_alphabet)))
    cipher_alphabet += ' '
    with open('./ciphers/simple_substitution_cipher/key.txt', 'w') as key_file:
        key_file.write(cipher_alphabet)


def get_key(path_to_key):
    with open(path_to_key, 'r') as key_file:
        global key
        key = key_file.readline().strip().upper()


def encrypt():
    get_key('./ciphers/simple_substitution_cipher/key.txt')
    with open('in.txt', 'r') as in_file:
        plain_text = in_file.readline().strip().upper()

    y = ''
    for x_i in plain_text:
        y += key[alphabet.index(x_i)]

    with open('./ciphers/simple_substitution_cipher/crypt.txt', 'w') as out_file:
        out_file.write(y)


def decrypt():
    get_key('./ciphers/simple_substitution_cipher/key.txt')
    with open('./ciphers/simple_substitution_cipher/crypt.txt', 'r') as in_file:
        cipher_text = in_file.readline().strip().upper()

    x = ''
    for y_i in cipher_text:
        x += alphabet[key.index(y_i)]

    with open('./ciphers/simple_substitution_cipher/decrypt.txt', 'w') as out_file:
        out_file.write(x)


if __name__ == '__main__':
    generate_key()
    encrypt()
    decrypt()
