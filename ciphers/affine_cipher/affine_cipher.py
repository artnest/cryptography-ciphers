import random
import string

alphabet = string.ascii_uppercase + ' '
key = alphabet
m = 26 + 1

a = 0
b = 0


def c_m(c):
    return alphabet.index(c)


def generate_key():
    cipher_alphabet = alphabet[:-1]
    cipher_alphabet = ''.join(random.sample(cipher_alphabet, 2))
    import math
    while math.gcd(alphabet.index(cipher_alphabet[0]), m) != 1:
        cipher_alphabet = ''.join(random.sample(cipher_alphabet, 2))
    with open('./ciphers/affine_cipher/key.txt', 'w') as key_file:
        key_file.write(cipher_alphabet)


def get_key(path_to_key):
    with open(path_to_key, 'r') as key_file:
        global key
        key = key_file.readline().strip().upper()

    global a, b
    a = c_m(key[0])
    b = c_m(key[1])
    import math
    assert math.gcd(a, m) == 1


def encrypt():
    get_key('./ciphers/affine_cipher/key.txt')
    with open('in.txt', 'r') as in_file:
        plain_text = in_file.readline().strip().upper()

    y = ''
    for x_i in plain_text:
        x = c_m(x_i)
        y += alphabet[(a * x + b) % m]

    with open('./ciphers/affine_cipher/crypt.txt', 'w') as out_file:
        out_file.write(y)


def decrypt():
    get_key('./ciphers/affine_cipher/key.txt')
    with open('./ciphers/affine_cipher/crypt.txt', 'r') as in_file:
        cipher_text = in_file.readline().strip().upper()

    x = ''
    for y_i in cipher_text:
        y = c_m(y_i)
        # from utils import euler_totient_function as phi
        # x += alphabet[int((y - b) * (a ** (phi(m) - 1)) % (m - 1))]
        x += alphabet[int((y - b) * (a ** -1) % (m - 1))]

    with open('./ciphers/affine_cipher/decrypt.txt', 'w') as out_file:
        out_file.write(x)


if __name__ == '__main__':
    generate_key()
    encrypt()
    decrypt()
