from caeser_cipher import CaesarCipher
from symmetric import SymmetricCipher
from asymmetric import AsymmetricCipher
from file_cipher import FileCipher
import base64


def run_program():
    print("===== Encrypted_Decrypted-app =====")
    print("Choose encryption type:")
    print("1. Caesar Cipher")
    print("2. Symmetric Encryption (Fernet)")
    print("3. Asymmetric Encryption (RSA)")
    print("4. File Encryption/Decryption (Fernet)")
    choice_type = input("Enter your choice (1, 2, 3, or 4): ")

    # ---------------------------
    # 1. Caesar Cipher
    # ---------------------------
    if choice_type == "1":
        cipher = CaesarCipher()
        print("\n--- Caesar Cipher ---")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        choice = input("Choose an option (1 or 2): ")

        # Caesar Cipher Encryption
        if choice == "1":
            plaintext = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            result = cipher.encrypt_caesar_cipher(plaintext, shift)
            print("Encrypted message:", result)

        # Caesar Cipher Decryption
        elif choice == "2":
            ciphertext = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            result = cipher.decrypt_caesar_cipher(ciphertext, shift)
            print("Decrypted message:", result)

        else:
            print("Invalid choice.")

    # ---------------------------
    # 2. Symmetric (Fernet)
    # ---------------------------
    elif choice_type == "2":
        print("\n--- Symmetric (Fernet) ---")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        choice = input("Choose an option (1 or 2): ")

        # Symmetric Encryption
        if choice == "1":
            cipher = SymmetricCipher()
            plaintext = input("Enter the message to encrypt: ")

            encrypted = cipher.encrypt(plaintext)
            print("Encrypted message:", encrypted.decode())
            print("Encryption key:", cipher.get_key().decode())

        # Symmetric Decryption
        elif choice == "2":
            key = input("Enter the encryption key: ").encode()
            cipher = SymmetricCipher(key)

            encrypted_input = input("Enter the message to decrypt: ").encode()

            try:
                decrypted = cipher.decrypt(encrypted_input)
                print("Decrypted message:", decrypted)
            except Exception as e:
                print("Error decrypting message:", e)

        else:
            print("Invalid choice.")

    # ---------------------------
    # 3. Asymmetric (RSA)
    # ---------------------------
    elif choice_type == "3":
        print("\n--- Asymmetric (RSA) ---")
        print("1. Encrypt a message (Public Key)")
        print("2. Decrypt a message (Private Key)")
        print("3. Generate a New RSA Key Pair")
        choice = input("Choose an option (1, 2, or 3): ")

        # Generate keys
        if choice == "3":
            cipher = AsymmetricCipher()
            print("\n--- New RSA Keys Generated ---")
            private_pem, public_pem = cipher.generate_keys()
            print("Private Key:\n", private_pem.decode())
            print("Public Key:\n", public_pem.decode())

        # RSA ENCRYPTION
        elif choice == "1":
            print("\nEnter Public Key:")
            public_key = ""
            print("Paste the public key (end with an empty line): ")
            while True:
                line = input()
                if line == "":
                    break
                public_key += line + "\n"
            cipher = AsymmetricCipher()

            message = input("Enter message to encrypt: ")

            #public_keys = input("Paste PUBLIC KEY:\n").encode()

            encrypted = cipher.encrypt(message, public_key.encode())
                

            print("\nEncrypted (Base64):")
            print(encrypted)

        # RSA DECRYPTION
        elif choice == "2":
            print("\nEnter Private Key:")
            private_key = ""
            print("Paste the private key (end with an empty line): ")
            while True:
                line = input()
                if line == "":
                    break
                private_key += line + "\n"

            cipher = AsymmetricCipher()

            encrypted_b64 = input("Enter Base64 encrypted message: ")
            

            try:
                decrypted = cipher.decrypt(encrypted_b64, private_key.encode())
                print("Decrypted message:", decrypted)
            except Exception as e:
                print("Error decrypting message:", e)


    # ---------------------------
    # 4. File Encryption/Decryption (Fernet)
    # ---------------------------   
    elif choice_type == "4":
        print("\n--- File Encryption/Decryption (Fernet) ---")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        choice = input("Choose an option (1 or 2): ")

        file_cipher = FileCipher()

        if choice == "1":
            filepath = input("Enter the path of the file to encrypt: ")
            key = file_cipher.generate_key()
            encrypted_file = file_cipher.encrypt_file(filepath, key)
            print(f"File encrypted: {encrypted_file}")
            print(f"Encryption key: {key.decode()}")

        elif choice == "2":
            filepath = input("Enter the path of the file to decrypt: ")
            key = input("Enter the encryption key: ").encode()
            try:
                decrypted_file = file_cipher.decrypt_file(filepath, key)
                print(f"File decrypted: {decrypted_file}")
            except Exception as e:
                print("Error decrypting file:", e)

        else:
            print("Invalid choice.")

    else:
        print("Invalid encryption type.")


if __name__ == "__main__":
    run_program()
