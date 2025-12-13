from src.file_cipher import FileCipher

def test_file_encrypt_decrypt(tmp_path):
    # create temp file
    original_file = tmp_path / "test.txt"
    original_content = "File encryption test"
    original_file.write_text(original_content)

    cipher = FileCipher()
    key = cipher.generate_key()  
    # encrypt
    encrypted_file_path = cipher.encrypt_file(str(original_file), key)
    
    # decrypt
    decrypted_file_path = cipher.decrypt_file(encrypted_file_path, key)

    # assert content matches
    decrypted_content = open(decrypted_file_path, "r").read()
    assert decrypted_content == original_content
