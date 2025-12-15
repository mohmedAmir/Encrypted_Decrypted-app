from cryptography.fernet import Fernet
import os

class FileCipher:

    def generate_key(self):
        """Generate a new Fernet key."""
        return Fernet.generate_key()
    def encrypt_file(self, filepath, key):
        """Encrypt a file using Fernet symmetric encryption and delete the original."""
        cipher = Fernet(key)

        with open(filepath, "rb") as f:
            data = f.read()

        encrypted_data = cipher.encrypt(data)

        encrypted_file = filepath + ".encrypted"
        with open(encrypted_file, "wb") as f:
            f.write(encrypted_data)

        # Remove the original file
    
        os.remove(filepath)

        return encrypted_file


    def decrypt_file(self, filepath, key):
        """Decrypt an encrypted file."""
        cipher = Fernet(key)

        with open(filepath, "rb") as f:
            encrypted_data = f.read()

        decrypted_data = cipher.decrypt(encrypted_data)

        output_file = filepath.replace(".encrypted", "")

        with open(output_file, "wb") as f:
            f.write(decrypted_data)

        return output_file
