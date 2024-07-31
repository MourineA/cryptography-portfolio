//Class Activity 1: Re-write XOR program to allow users to input  string variable and to enrypt the entered string 

#include <iostream>
#include <string>

using namespace std;

string encryptDecrypt(string toEncrypt) {
    char key = 'K'; // Any char will work
    string output = toEncrypt;
    
    for (int i = 0; i < toEncrypt.size(); i++)
        output[i] = toEncrypt[i] ^ key;
    
    return output;
}

int main() {
    string input;
    cout << "Enter a string to encrypt: ";
    getline(cin, input);
    
    string encrypted = encryptDecrypt(input);
    cout << "Encrypted: " << encrypted << "\n";
    
    string decrypted = encryptDecrypt(encrypted);
    cout << "Decrypted: " << decrypted << "\n";
    
    return 0;
}


