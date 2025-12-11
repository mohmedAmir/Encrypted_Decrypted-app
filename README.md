# **Encrypted_Decrypted-app**

A simple and user-friendly Python application that allows you to **Encrypt** and **Decrypt** messages using either the **Caesar Cipher** or **Symmetric Cipher (Fernet)**.
The app provides a **menu-based interface** where users can easily choose the cipher type and operation.

---

## **Features**

* **Caesar Cipher:**

  * Encrypt plaintext by shifting letters
  * Decrypt ciphertext back to the original message
  * Supports uppercase and lowercase letters
  * Preserves spaces, numbers, and punctuation

* **Symmetric Cipher (Fernet AES 128-bit):**

  * Encrypt and decrypt messages securely
  * Automatically generates encryption key
  * Prints key and encrypted message in copy-friendly format (no `b''`)

* Menu-based interface for easy operation

* Simple and beginner-friendly Python code

---

## **Installation**

1. **Clone this repository:**

```
git clone https://github.com/mohmedAmir/Encrypted_Decrypted-app.git
```

2. **Navigate into the project folder:**

```
cd Encrypted_Decrypted-app
```

3. **(Optional) Create and activate a Python virtual environment:**

### Windows (PowerShell):

```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### macOS/Linux:

```
python3 -m venv venv
source venv/bin/activate
```

4. **Install required libraries (for Symmetric Cipher):**

```
pip install cryptography
```

---

## **Running the Program**

Run the main program:

```
python main.py
```

You will see a menu like this:

```
===== Encryption/Decryption Program =====
Select cipher type:
1. Caesar Cipher
2. Symmetric Cipher (Fernet)
========================================
Choose an option:
```

## **Usage Examples**

### **1. Caesar Cipher**

* Choose `1` for Caesar Cipher
* **Encrypting a message:**

```
Enter your message: Hello 
Enter shift value: 3
Encrypted message: Khoor
```

* **Decrypting a message:**

```
Enter encrypted message: Khoor 
Enter shift value: 3
Decrypted message: Hello
```

---

### **2. Symmetric Cipher (Fernet)**

* Choose `2` for Symmetric Cipher
* **Encrypting a message:**

```
Enter your message: Hello world
Encrypted message: gAAAAABlZ...
Encryption key: R8IeyTp7BhqZICGGcDzJD9E0txcld105-G8kbGWiBY8=
```

* **Decrypting a message:**

```
Enter the encryption key: R8IeyTp7BhqZICGGcDzJD9E0txcld105-G8kbGWiBY8=
Enter the message to decrypt: gAAAAABlZ...
Decrypted message: Hello world
```

> ## The key and encrypted message are printed **without `b''`** so they are easy to copy and paste.

---

## **Notes**

* Always save the **encryption key** when using Symmetric Cipher; losing it means you cannot decrypt the message.
* Caesar Cipher only shifts letters; spaces, numbers, and punctuation remain unchanged.
* Shift values can be any integer. Positive numbers shift to the right, negative numbers shift to the left.
