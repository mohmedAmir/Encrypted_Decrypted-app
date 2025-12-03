from caeser_cipher import CaesarCipher
from symmetric import SymmetricCipher


def run_program():
    print("===== Encrypted_Decrypted-app =====")
    print("Choose encryption type:")
    print("1. Caesar Cipher")
    print("2. Symmetric Encryption (Fernet)")
    choice_type = input("Enter your choice (1 or 2): ")
    # CaesarCipher logic
    if choice_type == "1":
        cipher = CaesarCipher()
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        choice = input("Choose an option (1 or 2): ")
      # Encryption Caesar
        if choice == "1":
            plaintext = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            result = cipher.encrypt_caesar_cipher(plaintext, shift)
            print("Encrypted message:", result)
        # Decryption Caesar
        elif choice == "2":
            ciphertext = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            result = cipher.decrypt_caesar_cipher(ciphertext, shift)
            print("Decrypted message:", result)
        else:
            print("Invalid choice.")
   # SymmetricCipher logic
    elif choice_type == "2":
        cipher = SymmetricCipher()
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        choice = input("Choose an option (1 or 2): ")
        # Encryption Symmetric
        if choice == "1":
            plaintext = input("Enter the message to encrypt: ")
            encrypted = cipher.encrypt(plaintext)
            print("Encrypted message:", encrypted.decode())  
            print("Encryption key:", cipher.get_key().decode())
        # Decryption Symmetric
        elif choice == "2":
            key = input("Enter the encryption key: ").encode() 
            cipher = SymmetricCipher(key)
            
            encrypted_input = input("Enter the message to decrypt: ")
            
            try:
                # treat input as bytes
                ciphertext = encrypted_input.encode()
                decrypted = cipher.decrypt(ciphertext)
                print("Decrypted message:", decrypted)
            except Exception as e:
                print("Error decrypting message:", e)

        else:
            print("Invalid choice.")

    else:
        print("Invalid encryption type.")


if __name__ == "__main__":
    run_program()
