# making program to generate ROTx cipher and also decrypt it
# ROTx cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet.
# For example, with a shift of 1, A would be replaced by B, B would become C, and so on.

def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

#  main program
# while(True):
#     print("1. Encrypt")
#     print("2. Decrypt")
#     print("3. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         text = input("Enter text to encrypt: ")
#         shift = int(input("Enter shift: "))
#         print("Encrypted text: ", encrypt(text, shift))
#     elif choice == 2:
#         text = input("Enter text to decrypt: ")
#         shift = int(input("Enter shift: "))
#         print("Decrypted text: ", decrypt(text, shift))
#     elif choice == 3:
#         break
#     else:
#         print("Invalid choice")