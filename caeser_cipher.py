import string

class CaesarCipher:

    # Encrypt function
    def encrypt_caesar_cipher(self, plaintext, shift):
        encrypted_text = []
        for char in plaintext:
            if char in string.ascii_lowercase:
                index = (ord(char) - ord('a') + shift) % 26
                encrypted_text.append(chr(index + ord('a')))
            elif char in string.ascii_uppercase:
                index = (ord(char) - ord('A') + shift) % 26
                encrypted_text.append(chr(index + ord('A')))
            else:
                encrypted_text.append(char)
        return ''.join(encrypted_text)

    # Decrypt function
    def decrypt_caesar_cipher(self, ciphertext, shift):
        decrypted_text = []
        for char in ciphertext:
            if char in string.ascii_lowercase:
                index = (ord(char) - ord('a') - shift) % 26
                decrypted_text.append(chr(index + ord('a')))
            elif char in string.ascii_uppercase:
                index = (ord(char) - ord('A') - shift) % 26
                decrypted_text.append(chr(index + ord('A')))
            else:
                decrypted_text.append(char)
        return ''.join(decrypted_text)


# Run Caesar Cipher Program

'''
def run_program():
    cipher = CaesarCipher()

    print("===== Caesar Cipher Program =====")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("=================================")

    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        plaintext = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        result = cipher.encrypt_caesar_cipher(plaintext, shift)
        print("Encrypted message:", result)

    elif choice == "2":
        ciphertext = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        result = cipher.decrypt_caesar_cipher(ciphertext, shift)
        print("Decrypted message:", result)

    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    run_program()
'''
# The run_program function is commented out to avoid execution during imports.