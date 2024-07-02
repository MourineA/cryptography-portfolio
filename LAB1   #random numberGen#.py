import random

class PrimeKeyGenerator:
    def __init__(self, start=2, end=100):
        self.start = start
        self.end = end
        self.primes = self.generate_primes()

    def generate_primes(self):
        primes = []
        for num in range(self.start, self.end + 1):
            if self.is_prime(num):
                primes.append(num)
        return primes

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generate_keys(self):
        p = random.choice(self.primes)
        q = random.choice(self.primes)
        while q == p:
            q = random.choice(self.primes)
        return p, q

# Example usage
if __name__ == "__main__":
    key_gen = PrimeKeyGenerator()
    p, q = key_gen.generate_keys()
    print(f"Randomly generated prime numbers: p = {p}, q = {q}")
