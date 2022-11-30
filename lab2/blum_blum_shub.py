import sympy

class Blum_Blum_Shub():

    def __init__(self, seed):
        self.a = 2 * 10 ** 2
        self.b = 5 * 10 ** 2
        self.seed = seed

    def find_next_prime(self, number):
        p = sympy.nextprime(number)
        while p % 4 != 3:
            p = sympy.nextprime(p)
        return p

    def generate_random_number(self):
        p = self.find_next_prime(self.a)
        q = self.find_next_prime(self.b)
        n = p * q
        x_old = self.seed * self.seed % n
        for i in range(5):
            x = x_old * x_old % n
            x_old = x

        return x