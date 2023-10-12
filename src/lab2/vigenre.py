def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword.lower()
    for i in range(len(plaintext)):
        shift = ord(keyword[i % len(keyword)]) - ord('a')
        if plaintext[i].isupper():
            ciphertext += chr(ord('a') + (ord(plaintext[i].lower()) - ord('a') + shift) % 26).upper()
        else:
            ciphertext += chr(ord('a') + (ord(plaintext[i].lower()) - ord('a') + shift) % 26)

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword.lower()
    for i in range(len(ciphertext)):
        shift = ord(keyword[i % len(keyword)]) - ord('a')
        if ciphertext[i].isupper():
            plaintext += chr(ord('a') + (ord(ciphertext[i].lower()) - ord('a') - shift) % 26).upper()
        else:
            plaintext += chr(ord('a') + (ord(ciphertext[i].lower()) - ord('a') - shift) % 26)
    return plaintext

