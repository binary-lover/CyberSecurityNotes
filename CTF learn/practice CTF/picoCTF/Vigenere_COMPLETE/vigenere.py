import argparse

def get_padded_key(key, length):
    """Pad the key to match the length of the ciphertext."""
    new_key = key
    while len(new_key) < length:
        new_key += key
    return new_key[:length].lower()

def decrypt(ciphertext, key):
    """Decrypt the ciphertext using the Vigenère cipher."""
    plain_text = ""
    key = get_padded_key(key, len(ciphertext))
    key_indices = [ord(k) - ord('a') for k in key]  # Convert key letters to shifts

    key_index = 0
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():  # Check if the character is a letter
            shift = key_indices[key_index]  # Get the shift from the key
            if char.isupper():
                plain_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                plain_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            key_index += 1  # Only increment key index for letters
        else:
            plain_text += char  # Keep special characters unchanged

    return plain_text

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Decrypt a Vigenère cipher.')
    parser.add_argument('-c', '--cipher', type=str, required=True, help='Ciphertext to decrypt')
    parser.add_argument('-k', '--key', type=str, required=True, help='Key for decryption')

    args = parser.parse_args()

    # Decrypt the given ciphertext with the provided key
    decrypted_text = decrypt(args.cipher, args.key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()

