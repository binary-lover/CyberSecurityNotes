import argparse

def encrypt(text, rails):
    rail = [''] * rails
    direction_down = False
    row = 0

    for char in text:
        rail[row] += char
        if row == 0 or row == rails - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1

    return ''.join(rail)

def decrypt(cipher_text, rails):
    rail = [[''] * len(cipher_text) for _ in range(rails)]
    direction_down = None
    row, col = 0, 0

    for char in cipher_text:
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False

        rail[row][col] = '*'
        col += 1

        row += 1 if direction_down else -1

    index = 0
    for i in range(rails):
        for j in range(len(cipher_text)):
            if (rail[i][j] == '*' and index < len(cipher_text)):
                rail[i][j] = cipher_text[index]
                index += 1

    result = []
    row, col = 0, 0
    for char in cipher_text:
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False

        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1

        row += 1 if direction_down else -1

    return ''.join(result)

def main():
    parser = argparse.ArgumentParser(description='Rail Fence Cipher Encryption/Decryption.')
    parser.add_argument('-c', '--cipher', type=str, required=True, help='Path to the cipher text file')
    parser.add_argument('-d', '--depth', type=int, required=True, help='Number of rails (depth)')

    args = parser.parse_args()

    # Read the cipher text from the specified file
    with open(args.cipher, 'r') as file:
        cipher_text = file.read().strip()

    # Decrypt the cipher text
    decrypted_text = decrypt(cipher_text, args.depth)

    # Output the decrypted text
    print("Decrypted Text:")
    print(decrypted_text)

if __name__ == "__main__":
    main()

