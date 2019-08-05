import random
import string
import numpy as np

alphabet = string.ascii_uppercase + ' '
key = alphabet
m = 26 + 1


def generate_key():
    with open('in.txt') as f:
        n = len(f.readline().strip().upper())

    indices = [i for i in range(1, n + 1)]
    s_indices = random.sample(indices, len(indices))
    transposition = np.matrix((indices, s_indices))
    np.savetxt('./ciphers/transposition_cipher/key.txt', transposition, fmt='%d')


def get_key(path_to_key):
    global key
    key = np.loadtxt(path_to_key, dtype=int)


def encrypt():
    get_key('./ciphers/transposition_cipher/key.txt')

    with open('in.txt', 'r') as in_file:
        plain_text = in_file.readline().strip().upper()

    y = ''
    # for x_i, y_i in zip(plain_text, key[1, :]):
    for y_i in key[1]:
        y += plain_text[y_i - 1]

    with open('./ciphers/transposition_cipher/crypt.txt', 'w') as out_file:
        out_file.write(y)


def decrypt():
    get_key('./ciphers/transposition_cipher/key.txt')

    with open('./ciphers/transposition_cipher/crypt.txt', 'r') as in_file:
        cipher_text = in_file.readline().strip().upper()

    key[[0, 1]] = key[[1, 0]]
    inverse_key = sorted(zip(key[0], key[1]))
    key[0] = [x for x, _ in inverse_key]
    key[1] = [y for _, y in inverse_key]
    np.savetxt('./ciphers/transposition_cipher/inverse_key.txt', key, fmt='%d')

    x = ''
    for x_i in key[1]:
        x += cipher_text[x_i - 1]

    with open('./ciphers/transposition_cipher/decrypt.txt', 'w') as out_file:
        out_file.write(x)


if __name__ == '__main__':
    generate_key()
    encrypt()
    decrypt()
