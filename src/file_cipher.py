from cryptography.fernet import Fernet

class FileCipher:

    def generate_key(self):
        """Generate a new Fernet key."""
        return Fernet.generate_key()

    def encrypt_file(self, filepath, key):
        """Encrypt a file using Fernet symmetric encryption."""
        cipher = Fernet(key)

        with open(filepath, "rb") as f:
            data = f.read()

        encrypted_data = cipher.encrypt(data)

        with open(filepath + ".encrypted", "wb") as f:
            f.write(encrypted_data)

        return filepath + ".encrypted"

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
