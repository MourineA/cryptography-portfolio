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

    def euler_totient(self, n):
        result = n
        p = 2
        while p * p <= n:
            if n % p == 0:
                while n % p == 0:
                    n //= p
                result -= result // p
            p += 1
        if n > 1:
            result -= result // n
        return result

# Example usage
if __name__ == "__main__":
    key_gen = PrimeKeyGenerator()
    p, q = key_gen.generate_keys()
    print(f"Randomly generated prime numbers: p = {p}, q = {q}")

    n = p * q
    phi_n = key_gen.euler_totient(n)
    print(f"Euler's Totient Function value Φ({n}) = {phi_n}")
