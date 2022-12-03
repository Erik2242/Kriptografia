from solitare import Solitare
from blum_blum_shub import Blum_Blum_Shub

class Crypto():

    def __init__(self, generator_type, key):
        if generator_type == "Blum Blum Shub":
            generator = Blum_Blum_Shub(key)
        else:
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
