import sys

def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    key_int = [ord(i) - 97 for i in key.lower()]
    ciphertext_int = [ord(i) - 97 for i in ciphertext.lower()]
    
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_int[i % key_length]) % 26
        decrypted_text.append(chr(value + 97))

    return ''.join(decrypted_text)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python vigenere_decrypt.py <ciphertext> <key>")
        sys.exit(1)

    ciphertext = sys.argv[1]
    key = sys.argv[2]

    decrypted_message = vigenere_decrypt(ciphertext, key)
    print("picoCTF{"+decrypted_message+"}")

