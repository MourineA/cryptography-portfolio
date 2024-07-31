
//Part1

pip! install pycryptodome

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

def generate_keys():
    key = RSA.generate(1024)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_message(public_key, message):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted_message = cipher.encrypt(message)
    return encrypted_message

def decrypt_message(private_key, encrypted_message):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message
  
//Part(Server Code)
import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_keys():
    key = RSA.generate(1024)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def decrypt_message(private_key, encrypted_message):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message

def server_program():
    private_key, public_key = generate_keys()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(1)
    print("Server is listening...")

    conn, address = server_socket.accept()
    print(f"Connection from {address} has been established!")

    conn.send(public_key)
    encrypted_message = conn.recv(1024)
    decrypted_message = decrypt_message(private_key, encrypted_message)
    print(f"Decrypted message: {decrypted_message.decode()}")

    conn.close()

if __name__ == '__main__':
    server_program()
//Part3(Client side)
import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_message(public_key, message):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted_message = cipher.encrypt(message)
    return encrypted_message

def client_program():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))

    public_key = client_socket.recv(1024)
    message = b"Hello Bob, this is Alice"
    encrypted_message = encrypt_message(public_key, message)
    client_socket.send(encrypted_message)
    print(f"Encrypted message sent: {encrypted_message}")

    client_socket.close()

if __name__ == '__main__':
    client_program()


