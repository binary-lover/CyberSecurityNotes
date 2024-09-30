# here is the code algo
import ROTx

def getPaddedKey(key,length):
    newKey = key
    while len(newKey) < length:
        newKey += key

    if(newKey != length):
        newKey = newKey[:length]
    return newKey.lower()

def encrypt(text,key):
    cipher = ""
    key = getPaddedKey(key,len(text))
    # print(key,text)
    keyList = []
    for i in key:
        keyList.append( ord(i) - 97)
    # print(keyList)
    for i in range(len(key)):
        cipher+= (ROTx.encrypt(text[i],keyList[i]))
    print("cipher text: ",cipher)

def decrypt(text,key):
    plainText = ""
    key = getPaddedKey(key,len(text))
    keyList = []
    for i in key:
        keyList.append( ord(i) - 97)
    for i in range(len(key)):
        plainText+= (ROTx.decrypt(text[i],keyList[i]))
    print("paint text: ",plainText)
    

# encrypt("supersecreT","CODE")
# decrypt("uisitghgtsW","CODE")

while(True):
    print("1. Encrypt/Decrypt using Rotx")
    print("2. Encrypt/Decrypt using Vigenere")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Brute force encrypt")
        print("4. Brute force decrypt")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            text = input("Enter text to encrypt: ")
            shift = int(input("Enter shift: "))
            print("Encrypted text: ", ROTx.encrypt(text, shift))
        elif choice == 2:
            text = input("Enter text to decrypt: ")
            shift = int(input("Enter shift: "))
            print("Decrypted text: ", ROTx.decrypt(text, shift))
        elif choice == 3:
            text = input("Enter text to encrypt: ")
            rng = int(input("Enter range: "))
            ROTx.brute_force_encrypt(text,rng)
        elif choice == 4:
            text = input("Enter text to decrypt: ")
            rng = int(input("Enter range: "))
            ROTx.brute_force_decrypt(text,rng)
        else:
            print("Invalid choice")
    elif choice == 2:
        print("1. Encrypt")
        print("2. Decrypt")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            text = input("Enter text to encrypt: ")
            key = input("Enter key: ")
            encrypt(text,key)
        elif choice == 2:
            text = input("Enter text to decrypt: ")
            key = input("Enter key: ")
            decrypt(text,key)
        else:
            print("Invalid choice")
    elif choice == 3:
        break
    else:
        print("Invalid choice")
