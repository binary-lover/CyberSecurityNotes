import argparse
import string

def create_substitution_map(key):
    alphabet = string.ascii_uppercase  # Standard alphabet
    substitution_map = {alphabet[i]: key[i] for i in range(len(alphabet))}
    return substitution_map

def substitute(text, substitution_map):
    substituted = []
    for char in text:
        if char.upper() in substitution_map:
            new_char = substitution_map[char.upper()]
            substituted.append(new_char if char.isupper() else new_char.lower())
        else:
            substituted.append(char)  # Keep non-alphabetic characters unchanged
    return ''.join(substituted)

def read_key_from_file(key_file):
    with open(key_file, 'r') as file:
        key = file.read().strip()
    return key

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Substitute a monoalphabetic cipher using a key from a file.')
    parser.add_argument('-k', '--key', type=str, required=True, help='Path to the file containing the substitution key')

    args = parser.parse_args()

    # Read the key from the specified file
    key = read_key_from_file(args.key)

    # Validate key
    if len(key) != 26 or len(set(key)) != 26:
        print("Error: Key must be 26 unique uppercase letters.")
        return

    # Load the cipher text from a file
    with open('cipher.txt', 'r') as file:
        cipher_text = file.read()

    # Create the substitution map
    substitution_map = create_substitution_map(key)

    # Substitute the cipher text
    decoded_text = substitute(cipher_text, substitution_map)

    # Output the substituted text
    print("Decoded Text (Substituted):")
    print(decoded_text)

if __name__ == "__main__":
    main()

