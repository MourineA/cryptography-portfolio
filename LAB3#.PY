import random
import math

class RSA:
    def __init__(self):
        random.seed()

        # Step 1: Generate two large prime numbers, p and q
        self.p = self.generate_prime(24, 100)
        self.q = self.generate_prime(24, 100)

        # Step 2: Calculate n = p * q
        self.n = self.p * self.q

        # Step 3: Calculate Euler's totient function φ(n)
        self.phi_n = (self.p - 1) * (self.q - 1)

        # Step 4: Choose an integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
        self.e = self.generate_e(self.phi_n)

        # Step 5: Compute d as the modular multiplicative inverse of e modulo φ(n)
        self.d = self.modular_inverse(self.e, self.phi_n)

    def generate_prime(self, start, end):
        while True:
            num = random.randint(start, end)
            if self.is_prime(num):
                return num

    def is_prime(self, num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def generate_e(self, phi_n):
        while True:
            e = random.randint(2, phi_n - 1)
            if math.gcd(e, phi_n) == 1:
                return e

    def modular_inverse(self, a, m):
        m0, x0, x1 = m, 0, 1
        if m == 1:
            return 0
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += m0
        return x1

    def get_public_key(self):
        return self.e, self.n

    def get_private_key(self):
        return self.d, self.n

    def encrypt(self, message):
        ciphertext = ""
        for char in message:
            encrypted_char = pow(ord(char), self.e, self.n)
            ciphertext += str(encrypted_char) + " "
        return ciphertext.strip()

    def decrypt(self, ciphertext):
        decrypted_message = ""
        for num_str in ciphertext.split():
            num = int(num_str)
            decrypted_char = pow(num, self.d, self.n)
            decrypted_message += chr(decrypted_char)
        return decrypted_message

if __name__ == "__main__":
    rsa = RSA()

    # Generate key pair
    public_key = rsa.get_public_key()
    private_key = rsa.get_private_key()

    print(f"Public Key (e, n): {public_key}")
    print(f"Private Key (d, n): {private_key}")

    # Message to be encrypted
    message = "Hello, RSA!"
    print(f"\nOriginal Message: {message}")

    # Encrypt the message using the public key
    ciphertext = rsa.encrypt(message)
    print(f"Encrypted Message (Ciphertext): {ciphertext}")

    # Decrypt the ciphertext using the private key
    decrypted_message = rsa.decrypt(ciphertext)
    print(f"Decrypted Message: {decrypted_message}")
