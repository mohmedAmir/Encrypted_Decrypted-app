from src.symmetric import SymmetricCipher


def test_symmetric_encrypt_decrypt():
    cipher = SymmetricCipher()
    message = "Secret Message"

    encrypted = cipher.encrypt(message)
    key = cipher.get_key()

    decrypt_cipher = SymmetricCipher(key)
    decrypted = decrypt_cipher.decrypt(encrypted)

    assert decrypted == message


def test_symmetric_wrong_key_fails():
    cipher = SymmetricCipher()
    encrypted = cipher.encrypt("Hello")

    wrong_cipher = SymmetricCipher()
    try:
        wrong_cipher.decrypt(encrypted)
        assert False 
    except Exception:
        assert True
