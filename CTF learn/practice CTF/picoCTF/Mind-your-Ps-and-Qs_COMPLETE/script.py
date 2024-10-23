import gmpy2
from Crypto.Util.number import inverse

def rsa_decrypt(c, n, e):
    # Use gmpy2 to find prime factors
    p = gmpy2.is_prime(n)
    if not p:
        raise ValueError("Failed to factor n into two primes.")
    
    # Find factors using a simple trial division or advanced method
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            p = i
            q = n // i
            break
    else:
        raise ValueError("Failed to factor n into two primes.")

    # Calculate phi(n)
    phi = (p - 1) * (q - 1)

    # Calculate the modular inverse of e modulo phi(n)
    d = inverse(e, phi)

    # Decrypt the ciphertext
    decrypted_message = pow(c, d, n)

    return decrypted_message

# Example values
c = 843044897663847841476319711639772861390329326681532977209935413827620909782846667  # replace with your ciphertext
n = 1422450808944701344261903748621562998784243662042303391362692043823716783771691667  # replace with your modulus
e = 65537  # replace with your public exponent

# Decrypt the message
try:
    decrypted_message = rsa_decrypt(c, n, e)
    print(f"Decrypted message (as integer): {decrypted_message}")

    # Convert the decrypted integer to bytes and then to a string if needed
    decrypted_bytes = decrypted_message.to_bytes((decrypted_message.bit_length() + 7) // 8, 'big')
    print(f"Decrypted message (as string): {decrypted_bytes.decode('utf-8')}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"An error occurred: {e}")
