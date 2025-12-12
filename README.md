# Encrypted_Decrypted-app

**Encrypted_Decrypted-app** is a Python-based application designed to provide **easy, secure, and versatile encryption and decryption** options for both messages and files.  
It is suitable for beginners learning about cryptography as well as users who want a simple tool to protect sensitive data.

The project supports multiple encryption methods:

- **Caesar Cipher:** A classic, simple letter-shifting cipher for basic text obfuscation.  
- **Symmetric Cipher (Fernet AES 128-bit):** Modern symmetric encryption for secure message and file protection.  
- **Asymmetric Cipher (RSA 2048-bit):** Public/private key encryption for secure message exchange.  
- **File Encryption/Decryption (Fernet):** Encrypt and decrypt files while preserving the original file format.

**Purpose of the project:**

- Demonstrates different encryption techniques in one application.
- Provides hands-on experience with both classical and modern cryptography.
- Offers a practical tool to encrypt messages and files securely.
- Ensures copy-friendly handling of keys and encrypted data for easy sharing.

The app provides a **menu-driven interface**, allowing users to choose the type of encryption and operation without prior programming experience.

---
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> origin/main
## **Project Structure**
```
Encrypted_Decrypted-app/
│
├── src/
│ ├── main.py # Main program
│ ├── caeser_cipher.py # Caesar Cipher encryption
│ ├── symmetric.py # Symmetric encryption (Fernet)
│ ├── asymmetric.py # Asymmetric encryption (RSA)
│ └── file_cipher.py # File encryption/decryption
│
├── run.py # Easy way to run the application
├── requirements.txt # External dependencies
└── README.md
```
<<<<<<< HEAD
=======
>>>>>>> f3432b7127d05c9c6ccf953233b7dc9a0e286108
=======
>>>>>>> origin/main

## Features
...


### 1. Caesar Cipher
- Encrypt plaintext by shifting letters
- Decrypt ciphertext back to the original message
- Supports uppercase and lowercase letters
- Preserves spaces, numbers, and punctuation

### 2. Symmetric Cipher (Fernet AES 128-bit)
- Encrypt and decrypt messages securely
- Automatically generates encryption key
- Prints key and encrypted message in copy-friendly format (no `b''`)

### 3. Asymmetric Cipher (RSA 2048-bit)
- Generate RSA public/private key pair
- Encrypt messages using the public key
- Decrypt messages using the private key
- Messages are encoded in Base64 for safe copy/paste

### 4. File Encryption/Decryption (Fernet)
- Encrypt and decrypt files using a generated key
- Preserves the original file format after decryption
- Uses symmetric Fernet encryption for simplicity and security

---

## Installation

1. Clone this repository:

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
pip install -r requirements.txt
```
Running the Program

Run the program:
```
python run.py

```

### You will see a menu like this:
```
===== Encrypted_Decrypted-app =====
Choose encryption type:
1. Caesar Cipher
2. Symmetric Encryption (Fernet)
3. Asymmetric Encryption (RSA)
4. File Encryption/Decryption (Fernet)
Enter your choice (1, 2, 3, or 4):
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

# File Encryption/Decryption (Fernet)

Choose 4

## 1.Encrypt a file:
```
Enter the path of the file to encrypt:  C:\Users\desktop\example.txt
File encrypted:   C:\Users\desktop\example.txt.encrypted
Encryption key: R8IeyTp7BhqZICGGcDzJD9E0txcld105-G8kbGWiBY8=
```
## 2.Decrypt a file:
```
Enter the path of the file to decrypt: C:\Users\desktop\example.txt.encrypted
Enter the encryption key: R8IeyTp7BhqZICGGcDzJD9E0txcld105-G8kbGWiBY8=
File decrypted:  C:\Users\desktop\example.txt
```
### make sure that you copy the file path without " "

# Notes

Always save the encryption key for Symmetric Cipher; losing it means you cannot decrypt the message.

Caesar Cipher only shifts letters; spaces, numbers, and punctuation remain unchanged.

Shift values can be any integer. Positive numbers shift to the right, negative numbers shift to the left.

For Asymmetric Cipher, keep your private key safe; anyone with it can decrypt your messages.

All keys and messages are printed in copy-friendly formats.
