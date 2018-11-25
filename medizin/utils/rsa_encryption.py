from collections import namedtuple
import math
import random


class RSAEncryption(object):
    primes = namedtuple("primes", ["first_prime", "second_prime"])
    RSA_keys = namedtuple("RSA_keys", ["lock_key", "unlock_key", "mod_key"])

    def __init__(self):
        self.encrypt_key = None
        self.decipher_key = None
        self.common_modulus_key = None

    def get_encrypt_and_decipher_keys(self):
        self.generate_lock_and_unlock_tokens()
        if all([self.encrypt_key, self.decipher_key, self.common_modulus_key]):
            return self.RSA_keys(self.encrypt_key, self.decipher_key, self.common_modulus_key)
        else:
            return {"Message": "Sorry unable to generate encryption key"}

    @classmethod
    def is_prime(cls, number):
        if number in [2, 3]:
            return True  # number 2 and 3 are prime numbers

        # A prime number is divisible by only 1 and itself. When starting from 2 only factor left out is itself.
        for i in range(2, int(math.ceil((number + 1) / 2.0))):
            if number % i == 0:  # If divisible it is not a prime number
                return False
        return True

    @classmethod
    def is_co_prime(cls, number1, number2):
        # Two numbers are said to be co-prime if there are no common factors between them except 1
        for i in range(2, number1 if number1 >= number2 else number2):
            if number1 % i == 0 and number2 % i == 0:
                return False
        return True

    def generate_unique_prime_keys(self):
        first_prime = None
        second_prime = None
        while not all([first_prime, second_prime]):
            # number = random.randint(pow(10, 15), pow(10, 25))
            number = random.randint(2, 50)
            prime_status = self.is_prime(number)
            if prime_status and not first_prime:
                first_prime = number
            elif prime_status and not second_prime and number != first_prime:
                second_prime = number
        return self.primes(first_prime, second_prime)

    def generate_lock_and_unlock_tokens(self):
        # RSA token creation follows below algorithm
        # Step1: Select any two random large prime numbers
        prime_values = self.generate_unique_prime_keys()

        # Step2: Generate mod number which is product of above two prime numbers
        mod = prime_values.first_prime * prime_values.second_prime
        self.common_modulus_key = mod

        # Step3: order_of_n is the count of numbers that don't have common multiple with n.
        # If p and q are primes then the count would be (p-1)*(q-1)
        order_of_n = (prime_values.first_prime - 1) * (prime_values.second_prime - 1)

        # Step4: find encryption_key: It follows two conditions
        # 1 < encryption_key < order_of_n     and co-prime with mod and order_of_n
        for i in range(2, order_of_n):
            if self.is_co_prime(i, mod) and self.is_co_prime(i, order_of_n):
                self.encrypt_key = i

        # step5: find decipher_key: It should satisfy following condition:
        # (decipher_key * encryption_key) % order_of_n == 1

        i = 1
        while True:
            if (i * self.encrypt_key) % order_of_n == 1 and i != self.encrypt_key:
                self.decipher_key = i
                break
            i = i + 1
