def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON", 0)
    'SBWKRQ'
    >>> encrypt_caesar("python", 0)
    'sbwkrq'
    >>> encrypt_caesar("Python3.6", 0)
    'Sbwkrq3.6'
    >>> encrypt_caesar("", 120)
    ''
    """
    ciphertext = ""
    shift %= 26
    for i in plaintext:
        if i.isalpha() and i.islower():
            ciphertext += chr(ord('a') + (ord(i) - ord('a') + shift) % 26)
        elif i.isalpha() and i.isupper():
            ciphertext += chr(ord('A') + (ord(i) - ord('A') + shift) % 26)
        else:
            ciphertext += i

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    # shift %= 26
    # for i in ciphertext:
    #     if i.isalpha() and i.islower():
    #         plaintext += chr(ord('a') + (ord(i) - ord('a') - shift) % 26)
    #     elif i.isalpha() and i.isupper():
    #         plaintext += chr(ord('A') + (ord(i) - ord('A') - shift) % 26)
    #     else:
    #         plaintext += i
    return plaintext



