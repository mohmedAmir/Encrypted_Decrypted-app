import base64
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding


class AsymmetricCipher:

    def generate_keys(self):
        """
        Generate RSA public and private keys in PEM format.
        Returns: (private_key_pem, public_key_pem)
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        public_key = private_key.public_key()

        # Export private key in PEM format
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        # Export public key in PEM format
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        return private_pem, public_pem

    def encrypt(self, message, public_pem):
        """
        Encrypt a message using the RSA public key.
        Output is Base64 encoded string.
        """
        public_key = serialization.load_pem_public_key(public_pem)

        encrypted_bytes = public_key.encrypt(
            message.encode(),   # message must be string here
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # Convert raw bytes → Base64 string
        return base64.b64encode(encrypted_bytes).decode()

    def decrypt(self, encrypted_b64, private_pem):
        """
        Decrypt a Base64 encrypted message using RSA private key.
        """
        private_key = serialization.load_pem_private_key(private_pem, password=None)

        encrypted_bytes = base64.b64decode(encrypted_b64)

        decrypted_bytes = private_key.decrypt(
            encrypted_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return decrypted_bytes.decode()
