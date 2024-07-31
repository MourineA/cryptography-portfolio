//Implementing Caesar Cipher in Python(It works by shifting the  letters in the plaintext by a fixed number of positions down or up the alphabet.

//Encryption
def encrypt_caesar_cipher(plaintext, shift):
    encrypted_message = ""
    for char in plaintext:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_message += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            encrypted_message += char
    return encrypted_message

# Example usage
plaintext = "HELLO, World!"
shift = 3
encrypted_message = encrypt_caesar_cipher(plaintext, shift)
print(f"Encrypted message: {encrypted_message}")
//Decryption
def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_message = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            decrypted_message += chr((ord(char) - shift - shift_amount) % 26 + shift_amount)
        else:
            decrypted_message += char
    return decrypted_message

# Example usage
ciphertext = encrypted_message  # Use the encrypted message from the previous example
decrypted_message = decrypt_caesar_cipher(ciphertext, shift)
print(f"Decrypted message: {decrypted_message}")
//Handling the output

def encrypt_caesar_cipher(plaintext, shift):
    encrypted_message = ""
    for char in plaintext:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_message += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_message = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            decrypted_message += chr((ord(char) - shift - shift_amount) % 26 + shift_amount)
        else:
            decrypted_message += char
    return decrypted_message

if __name__ == "__main__":
    mode = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()
    text = input("Enter your message: ").strip()
    shift = int(input("Enter shift value: ").strip())

    if mode == 'e':
        result = encrypt_caesar_cipher(text, shift)
    elif mode == 'd':
        result = decrypt_caesar_cipher(text, shift)
    else:
        result = "Invalid mode selected."

    print(f"Result: {result}")

