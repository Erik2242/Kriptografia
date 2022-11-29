from random import seed, randint, shuffle
from solitare import Solitare


def encrypt(text, key):
    seed(key)
    result = ""
    for letter in text:
        result = result + chr((ord(letter) + randint(0, 255)) % 255)
    return result

def decrypt(text, key):
    seed(key)
    result = ""
    for letter in text:
        result = result + chr((ord(letter) + 255 - randint(0, 255)) % 255 )
    return result

def main():
    # res = encrypt("AbraCada371nd!';]", "ami")
    # print(decrypt(res, "ami"))
    deck = list(range(1,55))
    shuffle(deck)
    solitare1 = Solitare(deck.copy())
    solitare2 = Solitare(deck.copy())
    print(solitare1.shuffle())
    print(solitare2.shuffle())
    


if __name__ == "__main__":
    main()