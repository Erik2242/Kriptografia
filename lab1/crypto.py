#!/usr/bin/env python3 -tt
import numpy as np

"""
File: crypto.py
---------------
Assignment 1: Cryptography
Course: CS 41
Name: Horvath Erik
SUNet: heim1919

Replace this with a description of the program.
"""
import utils

# Caesar Cipher

def encrypt_caesar(plaintext):
    """Encrypt plaintext using a Caesar cipher.

    Add more implementation details here.
    """
    result = ""
    for letter in plaintext:
        result += chr((ord(letter) - 62) % 26 + 65)
    return result
    

def decrypt_caesar(ciphertext):
    """Decrypt a ciphertext using a Caesar cipher.

    Add more implementation details here.
    """
    result = ""
    for letter in ciphertext:
        result += chr((ord(letter) - 68) % 26 + 65)
    return result


# Vigenere Cipher

def set_keyword(plaintext, keyword):
    final_keyword = ""
    i = 0
    for letter in plaintext:
        if i == len(keyword):
            i = 0
        final_keyword = final_keyword + keyword[i]
        i += 1
    return final_keyword

def encrypt_vigenere(plaintext, keyword):
    keyword = set_keyword(plaintext, keyword)
    result = ""
    for i in range(len(plaintext)):
        result += chr((ord(plaintext[i]) + ord(keyword[i]) - 130) % 26 + 65)
    return result


def decrypt_vigenere(ciphertext, keyword):
    keyword = set_keyword(ciphertext, keyword)
    result = ""
    for i in range(len(ciphertext)):
        result += chr((ord(ciphertext[i]) - ord(keyword[i]) - 130) % 26 + 65)
    return result


def encrypt_scytale(plaintext, n):
    rows = n
    columns = len(plaintext)
    matrix = np.full((rows, columns), "")
    i = 0
    j = 0
    for letter in plaintext:
        if i == rows:
            i = 0
        matrix[i][j] = letter
        i += 1
        j += 1
    result = ""
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] != "":
                result += matrix[i][j]
    return result


def make_scytale_matrix(matrix, rows, columns):
    i = 0
    j = 0
    while j < columns:
        if i == rows:
            i = 0
        matrix[i][j] = "*"
        i += 1
        j += 1
    return matrix


def decrypt_scytale(ciphertext, n):
    rows = n
    columns = len(ciphertext)
    matrix = make_scytale_matrix(np.full((rows, columns), ""), rows, columns)
    result = ""
    k = 0
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == "*":
                matrix[i][j] = ciphertext[k]
                k += 1
    result = ""
    i = 0
    j = 0
    while j < columns:
        if i == rows:
            i = 0
        result += matrix[i][j]
        i += 1
        j += 1
    return result


def encrypt_railfence(plaintext, n):
    rows = n
    columns = len(plaintext)
    matrix = np.full((rows, columns), "")

    i = 0
    j = 0
    increment = -1
    for letter in plaintext:
        if i == n - 1 or i == 0:
            increment = increment * (-1)
        matrix[i][j] = letter
        i += increment
        j += 1
    result = ""
    i = 0
    j = 0
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] != "":
                result += matrix[i][j]
    return result


def make_zig_zag(matrix, rows, columns):
    i = 0
    j = 0
    increment = -1
    while j < columns:
            if i == rows - 1 or i == 0:
                increment = increment * (-1)
            matrix[i][j] = "*"
            i += increment
            j += 1
            
    return matrix


def decrypt_railfence(ciphertext, n):
    rows = n
    columns = len(ciphertext)
    matrix = np.full((rows, columns), "")
    matrix = make_zig_zag(matrix, rows, columns)
    k = 0
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == "*":
                matrix[i][j] = ciphertext[k]
                k += 1
    result = ""
    i = 0
    j = 0
    increment = -1
    while j < columns:
        if i == n - 1 or i == 0:
            increment = increment * (-1)
        result += matrix[i][j]
        i += increment
        j += 1
        
    return result


def main():
    # print(encrypt_caesar("PYTHON"))
    # print(decrypt_caesar("SBWKRQ"))
    # print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))
    # print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))
    # print(encrypt_railfence("WEAREDISCOVEREDFLEEATONCE", 3))
    # print(decrypt_railfence("WECRLTEERDSOEEFEAOCAIVDEN", 3))
    print(encrypt_scytale("IAMHURTVERYBADLYHELP", 5))
    print(decrypt_scytale("IRYYATBHMVAEHEDLURLP", 5))



# Merkle-Hellman Knapsack Cryptosystem

def generate_private_key(n=8):
    """Generate a private key for use in the Merkle-Hellman Knapsack Cryptosystem.

    Following the instructions in the handout, construct the private key components
    of the MH Cryptosystem. This consistutes 3 tasks:

    1. Build a superincreasing sequence `w` of length n
        (Note: you can check if a sequence is superincreasing with `utils.is_superincreasing(seq)`)
    2. Choose some integer `q` greater than the sum of all elements in `w`
    3. Discover an integer `r` between 2 and q that is coprime to `q` (you can use utils.coprime)

    You'll need to use the random module for this function, which has been imported already

    Somehow, you'll have to return all of these values out of this function! Can we do that in Python?!

    @param n bitsize of message to send (default 8)
    @type n int

    @return 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.
    """
    raise NotImplementedError  # Your implementation here

def create_public_key(private_key):
    """Create a public key corresponding to the given private key.

    To accomplish this, you only need to build and return `beta` as described in the handout.

        beta = (b_1, b_2, ..., b_n) where b_i = r ?? w_i mod q

    Hint: this can be written in one line using a list comprehension

    @param private_key The private key
    @type private_key 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.

    @return n-tuple public key
    """
    raise NotImplementedError  # Your implementation here


def encrypt_mh(message, public_key):
    """Encrypt an outgoing message using a public key.

    1. Separate the message into chunks the size of the public key (in our case, fixed at 8)
    2. For each byte, determine the 8 bits (the `a_i`s) using `utils.byte_to_bits`
    3. Encrypt the 8 message bits by computing
         c = sum of a_i * b_i for i = 1 to n
    4. Return a list of the encrypted ciphertexts for each chunk in the message

    Hint: think about using `zip` at some point

    @param message The message to be encrypted
    @type message bytes
    @param public_key The public key of the desired recipient
    @type public_key n-tuple of ints

    @return list of ints representing encrypted bytes
    """
    raise NotImplementedError  # Your implementation here

def decrypt_mh(message, private_key):
    """Decrypt an incoming message using a private key

    1. Extract w, q, and r from the private key
    2. Compute s, the modular inverse of r mod q, using the
        Extended Euclidean algorithm (implemented at `utils.modinv(r, q)`)
    3. For each byte-sized chunk, compute
         c' = cs (mod q)
    4. Solve the superincreasing subset sum using c' and w to recover the original byte
    5. Reconsitite the encrypted bytes to get the original message back

    @param message Encrypted message chunks
    @type message list of ints
    @param private_key The private key of the recipient
    @type private_key 3-tuple of w, q, and r

    @return bytearray or str of decrypted characters
    """
    raise NotImplementedError  # Your implementation here


if __name__ == "__main__":
    main()
