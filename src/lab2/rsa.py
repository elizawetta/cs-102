import random
import typing as tp


def is_prime(n: int) -> bool:
    """
    Input: n - number to check 
    Tests to see if a number is prime.
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    >>> is_prime(1)
    False
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """
    Input: a, b - numbers 
    Output: greatest common divisor a and b
    Euclid's algorithm for determining the greatest common divisor.
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    a, b = max(a, b), min(a, b)
    while a % b != 0:
        a, b = b, a % b
    return b


def multiplicative_inverse(e: int, phi: int) -> int:
    """
    Input: 
    e - prime number
    phi - Euler function 
    Output: result of multiplicative inverse e and phi
    
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.
    >>> multiplicative_inverse(7, 40)
    23
    """
    a = phi
    b = e
    lst = []
    while a % b != 0:
        lst.append([a, b, a % b, a//b, 0, 0])
        a, b = b, a % b
    lst.append([a, b, a % b, a//b, 0, 1])
    for i in range(len(lst) - 2, -1, -1):
        lst[i][4] = lst[i + 1][5]
        lst[i][5] = lst[i + 1][4] - lst[i + 1][5] * lst[i][3]
    return lst[0][-1] % phi


def generate_keypair(p: int, q: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    '''
    Input: p, q - prime numbers
    Output: tuple of public key and  private key
    
    Generating keypair
    '''
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal")

    n = p*q

    phi = (p-1)*(q-1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return (e, n), (d, n)


def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    '''
    Input: pk - private key, plaintext - text to encryption
    Output: cipher - encrypted text
    
    Encryption function
    '''
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    '''
    Input: pk - public key, plaintext - text to decryption
    Output: cipher - decrypted text

    Decryption function
    '''
    
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return "".join(plain)


if __name__ == "__main__":
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print("".join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))

