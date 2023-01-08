from solitare import Solitare

class Crypto():

    def __init__(self, generator_type, key):
        generator = Solitare(key)
        self.shift = generator.generate_random_number()
        


    def encrypt(self, text):
        result = ""
        for letter in text:
            result = result + chr((ord(letter) + self.shift) % 255)
        return result

    def decrypt(self, text):
        result = ""
        for letter in text:
            result = result + chr((ord(letter) + 255 - self.shift) % 255)
        return result
