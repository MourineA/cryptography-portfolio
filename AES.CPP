#include <iostream>
#include <string>
#include <cryptopp/cryptlib.h>
#include <cryptopp/aes.h>
#include <cryptopp/modes.h>
#include <cryptopp/filters.h>
#include <cryptopp/osrng.h>

using namespace CryptoPP;
using namespace std;

string encrypt(const string& plainText, const SecByteBlock& key, const byte iv[AES::BLOCKSIZE]) {
    string cipherText;
    try {
        CBC_Mode<AES>::Encryption encryption;
        encryption.SetKeyWithIV(key, key.size(), iv);

        StringSource(plainText, true, 
            new StreamTransformationFilter(encryption,
                new StringSink(cipherText)
            )
        );
    } catch(const Exception& e) {
        cerr << e.what() << endl;
        exit(1);
    }
    return cipherText;
}

string decrypt(const string& cipherText, const SecByteBlock& key, const byte iv[AES::BLOCKSIZE]) {
    string plainText;
    try {
        CBC_Mode<AES>::Decryption decryption;
        decryption.SetKeyWithIV(key, key.size(), iv);

        StringSource(cipherText, true,
            new StreamTransformationFilter(decryption,
                new StringSink(plainText)
            )
        );
    } catch(const Exception& e) {
        cerr << e.what() << endl;
        exit(1);
    }
    return plainText;
}

int main() {
    AutoSeededRandomPool prng;

    // Generate a random key and IV
    SecByteBlock key(AES::DEFAULT_KEYLENGTH);
    prng.GenerateBlock(key, key.size());

    byte iv[AES::BLOCKSIZE];
    prng.GenerateBlock(iv, sizeof(iv));

    // Prompt the user to enter a string to encrypt
    string plainText;
    cout << "Enter a string to encrypt: ";
    getline(cin, plainText);

    // Encrypt the plain text
    string cipherText = encrypt(plainText, key, iv);
    cout << "Encrypted: " << cipherText << endl;

    // Decrypt the cipher text
    string decryptedText = decrypt(cipherText, key, iv);
    cout << "Decrypted: " << decryptedText << endl;

    return 0;
}
