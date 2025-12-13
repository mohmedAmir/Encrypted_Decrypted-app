from src.asymmetric import AsymmetricCipher


def test_rsa_encrypt_decrypt():
    cipher = AsymmetricCipher()

    private_key, public_key = cipher.generate_keys()
    message = "Hello RSA"

    encrypted = cipher.encrypt(message, public_key)
    decrypted = cipher.decrypt(encrypted, private_key)

    assert decrypted == message


def test_rsa_wrong_private_key_fails():
    cipher1 = AsymmetricCipher()
    cipher2 = AsymmetricCipher()

    priv1, pub1 = cipher1.generate_keys()
    priv2, _ = cipher2.generate_keys()

    encrypted = cipher1.encrypt("Test", pub1)

    try:
        cipher1.decrypt(encrypted, priv2)
        assert False
    except Exception:
        assert True
