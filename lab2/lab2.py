from random import seed, randint


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
    res = encrypt("AbraCada371nd!';]", "ami")
    print(decrypt(res, "ami"))


if __name__ == "__main__":
    main()