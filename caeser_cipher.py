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
    