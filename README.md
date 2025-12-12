# Encrypted_Decrypted-app

A simple and user-friendly Python application that allows you to Encrypt and Decrypt messages using Caesar Cipher, Symmetric Cipher (Fernet), or Asymmetric Cipher (RSA).
The app provides a menu-based interface for easy selection of cipher type and operation.

# Features

## Caesar Cipher:

Encrypt plaintext by shifting letters

Decrypt ciphertext back to the original message

Supports uppercase and lowercase letters

Preserves spaces, numbers, and punctuation

## Symmetric Cipher (Fernet AES 128-bit):

Encrypt and decrypt messages securely

Automatically generates encryption key

Prints key and encrypted message in copy-friendly format (no b'')

## Asymmetric Cipher (RSA 2048-bit):

Generate RSA public/private key pair

Encrypt messages using the public key

Decrypt messages using the private key

Messages are encoded in Base64 for safe copy/paste

Menu-based interface for easy operation

Beginner-friendly Python code

# Installation

Clone this repository:
```
git clone https://github.com/mohmedAmir/Encrypted_Decrypted-app.git
```

Navigate into the project folder:
```
cd Encrypted_Decrypted-app
```

(Optional) Create and activate a Python virtual environment:

Windows (PowerShell):
```
python -m venv venv
.\venv\Scripts\Activate.ps1
```
macOS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

Install required libraries:
```
pip install cryptography
```
Running the Program

Run the main program:
```
python main.py
```

You will see a menu like this:
```
===== Encrypted_Decrypted-app =====
Choose encryption type:
1. Caesar Cipher
2. Symmetric Encryption (Fernet)
3. Asymmetric Encryption (RSA)
Enter your choice (1, 2, or 3):
```
## Usage Examples:

# 1. Caesar Cipher
   
Choose 1

## Encrypting a message:
```
Enter your message: Hello
Enter the shift value: 3
Encrypted message: Khoor
```

## Decrypting a message:
```
Enter the message to decrypt: Khoor
Enter the shift value: 3
Decrypted message: Hello
```
# 2. Symmetric Cipher (Fernet)

Choose 2

## Encrypting a message:
```
Enter your message: Hello World
Encrypted message: gAAAAABlZ...
Encryption key: R8IeyTp7BhqZICGGcDzJD9E0txcld105-G8kbGWiBY8=
```

## Decrypting a message:
```
Enter the encryption key: R8IeyTp7BhqZICGGcDzJD9E0txcld105-G8kbGWiBY8=
Enter the message to decrypt: gAAAAABlZ...
Decrypted message: Hello World
```

### Messages and keys are printed without b'' for easy copy/paste.

# 3. Asymmetric Cipher (RSA 2048-bit)

Choose 3
```
Generate RSA keys:

--- New RSA Keys Generated ---
Private Key:
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqh...
-----END PRIVATE KEY-----
Public Key:
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhki...
-----END PUBLIC KEY-----

```
## Encrypt a message using the public key:
```
Enter Public Key (paste, end with empty line):
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhki...
-----END PUBLIC KEY-----

Enter message to encrypt: Hello RSA
Encrypted (Base64):
Ih9VOP/TnwWE3ZkGEIKztsfND/D7aK0bHUBL1dv5xGvo6uKoQnKuC0i3...
```

## Decrypt a message using the private key:
```
Enter Private Key (paste, end with empty line):
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqh...
-----END PRIVATE KEY-----

Enter Base64 encrypted message: Ih9VOP/TnwWE3ZkGEIKztsfND/D7aK0bHUBL1dv5xGvo6uKoQnKuC0i3...
Decrypted message: Hello RSA
```

### Messages are Base64 encoded for safe copy/paste.

# Notes

Always save the encryption key for Symmetric Cipher; losing it means you cannot decrypt the message.

Caesar Cipher only shifts letters; spaces, numbers, and punctuation remain unchanged.

Shift values can be any integer. Positive numbers shift to the right, negative numbers shift to the left.

For Asymmetric Cipher, keep your private key safe; anyone with it can decrypt your messages.

All keys and messages are printed in copy-friendly formats.
