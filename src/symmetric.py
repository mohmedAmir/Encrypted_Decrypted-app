
from cryptography.fernet import Fernet


class SymmetricCipher:
    """
    Symmetric encryption using Fernet (AES 128-bit with HMAC for integrity).
    """

    def __init__(self, key=None):
        """
        Initialize the cipher.
        If no key is provided, generate a new key.
        """
        if key:
            self.key = key
        else:
            self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, plaintext):
        """
        Encrypt a plaintext string.
        :param plaintext: str
        :return: bytes (ciphertext)
        """
        return self.cipher.encrypt(plaintext.encode())

    def decrypt(self, ciphertext):
        """
        Decrypt a ciphertext.
        :param ciphertext: bytes
        :return: str (plaintext)
        """
        return self.cipher.decrypt(ciphertext).decode()

    def get_key(self):
        """
        Return the current key (for sharing or saving).
        """
        return self.key
