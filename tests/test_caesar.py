from src.caeser_cipher import CaesarCipher


def test_caesar_encrypt_basic():
    cipher = CaesarCipher()
    encrypted = cipher.encrypt_caesar_cipher("Hello", 3)
    assert encrypted == "Khoor"


def test_caesar_decrypt_basic():
    cipher = CaesarCipher()
    decrypted = cipher.decrypt_caesar_cipher("Khoor", 3)
    assert decrypted == "Hello"


def test_caesar_preserves_symbols():
    cipher = CaesarCipher()
    text = "Hello, World! 123"
    encrypted = cipher.encrypt_caesar_cipher(text, 5)
    decrypted = cipher.decrypt_caesar_cipher(encrypted, 5)
    assert decrypted == text
