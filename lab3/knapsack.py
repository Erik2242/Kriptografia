import random
import utils

class Knapsack():

    def __init__(self, n = 8):
        self.n = n

    def generate_private_key(self):
        w = self.generate_w()
        q = random.randint(sum(w) + 1, 2 * sum(w))
        r = random.randint(2, q - 1)
        while not is_coprime(r, q):
            r = random.randint(2, q - 1)
        self.private_key = (w, q, r)
        return self.private_key

    def create_public_key(self):
        self.beta = []
        r = self.private_key[2]
        q = self.private_key[1]
        w = self.private_key[0]
        for i in range(8):
            self.beta = self.beta + [r * w[i] % q]
        return self.beta

    def generate_w(self):
        starter = random.randint(2, 10)
        w = [starter]
        while len(w) < self.n:
            total = sum(w)
            w = w + [random.randint(total + 1, 2 * total)]
        return w

    def encrypt(self, message):
        result = []
        split_message = [message[i:i+self.n] for i in range(0, len(message), self.n)]
        for chunk in split_message:
            byte_result = []
            for byte in chunk:
                bits = list(map(lambda x: int(x), '{0:08b}'.format(ord(byte))))
                c = 0
                for i in range(7):
                    c = c + bits[i] * self.beta[i]
                byte_result = byte_result + [c]
            result = result + [byte_result]
                
        return result

def gcd(p,q):
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    return gcd(x, y) == 1
