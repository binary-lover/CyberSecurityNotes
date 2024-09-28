# Cryptography notes

## Types of ciphers

### XOR cipher

XOR cipher is a simple additive encryption technique in itself. It is sometimes used for encrypting text for storage. It is not a secure encryption technique by itself. The basic principle of the XOR cipher is that it will take an input and XOR it with a key to produce an encrypted output. The same key is then used to decrypt the message.

The XOR cipher is a symmetric key cipher, which means that the same key is used for both encryption and decryption. The XOR cipher is also known as the Vernam cipher, named after Gilbert Vernam, who patented the cipher in 1919.

here is an example of XOR cipher:

```python
def xor_cipher(text, key):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))

text = "Hello
key = "key"
encrypted_text = xor_cipher(text, key)
print(encrypted_text)
```
for decryption, you can use the same function with the same key.

```python
decrypted_text = xor_cipher(encrypted_text, key)
print(decrypted_text)
```

### Caesar cipher

The Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down the alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on.

The Caesar cipher is named after Julius Caesar, who is said to have used it to communicate with his generals. It is also known as a shift cipher, Caesar's code, or Caesar shift.

Here is an example of Caesar cipher: click [here](./ROTx.py) see the code.

### Vigenère cipher

The Vigenère cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. A polyalphabetic cipher uses multiple substitution alphabets to encrypt the text. The Vigenère cipher is a form of the Caesar cipher, but instead of using a single shift value, it uses a keyword to determine the shift value for each letter in the plaintext.

The Vigenère cipher is named after Blaise de Vigenère, a French diplomat who lived in the 16th century. It was first described by Giovan Battista Bellaso in his 1553 book La cifra del. Sig. Giovan Battista Bellaso.

Here is an example of Vigenère cipher: click [here](./vigenere.py) see the code.

### Rail Fence cipher

The Rail Fence cipher is a form of transposition cipher that gets its name from the way it encrypts the message. The message is written in a zigzag pattern on a rail fence, and then the letters are read off in rows to produce the ciphertext.

The Rail Fence cipher is a simple and easy-to-implement encryption technique that can be used to encrypt messages. It is not a secure encryption technique by itself, but it can be combined with other encryption techniques to provide additional security.

```python
def rail_fence_encrypt(text, key):
    fence = [[] for _ in range(key)]
    rail = 0
    direction = 1

    for char in text:
        fence[rail].append(char)
        rail += direction

        if rail == key - 1 or rail == 0:
            direction = -direction

    return ''.join(''.join(row) for row in fence)

text = "Hello, World!"
key = 3
encrypted_text = rail_fence_encrypt(text, key)

print(encrypted_text)
```

for decryption, you can use the following code:

```python

def rail_fence_decrypt(text, key):
    fence = [[] for _ in range(key)]
    rail = 0
    direction = 1

    for char in text:
        fence[rail].append(char)
        rail += direction

        if rail == key - 1 or rail == 0:
            direction = -direction

    index = 0
    result = ''
    for _ in range(len(text)):
        for row in fence:
            if index < len(row):
                result += row[index]
        index += 1

    return result


decrypted_text = rail_fence_decrypt(encrypted_text, key)

print(decrypted_text)
```

## Hashing Functions

### What is a hashing function?

A hashing function is a mathematical function that takes an input (or "message") and returns a fixed-size string of bytes. The output, known as the hash value, is typically a fixed-size string of bytes. Hash functions are commonly used in computer science and cryptography to generate a unique value for a given input. eg. `md5`, `sha1`, `sha256`, `sha512`, etc.

### Cryptographic Vs Non-Cryptographic Hash Functions


| Cryptographic Hash Functions | Non-Cryptographic Hash Functions |
|------------------------------|-----------------------------------|
| Secure                       | Not secure                        |
| Collision-resistant          | Not collision-resistant           |
| One-way                      | Two-way                           |
| Deterministic                | Non-deterministic                 |
| Fixed-size output            | Variable-size output              |
| Slow                         | Fast                              |

### Properties of Cryptographic Hash Functions

1. Deterministic: The same input will always produce the same output.
2. Fast: The hash function should be computationally efficient.
3. Fixed-size output: The hash function should produce a fixed-size output.
4. Collision-resistant: It should be difficult to find two different inputs that produce the same output.
5. Pre-image resistance: Given a hash value, it should be difficult to find the original input.
6. Second pre-image resistance: Given an input, it should be difficult to find a different input that produces the same hash value.

### Common Hash Functions

- [MD5](#md5) (Message Digest Algorithm 5)
- [SHA1](#sha1) (Secure Hash Algorithm 1)
- [SHA256](#sha256) (Secure Hash Algorithm 256)
- [SHA512](#sha512) (Secure Hash Algorithm 512)
- [HMAC](#hmac) (Hash-based Message Authentication Code)



### MD5
- MD% (Message Digest Algorithm 5)
- Bite size: 128
- Output size: 32
- Collision: Yes
- Speed: Fast
- Security: Weak

```python   
import hashlib
print(hashlib.md5(b"Hello, World!").hexdigest())
```

### SHA1
- SHA (Secure Hash Algorithm)
- Bite size: 160
- Output size: 40
- Collision: Yes
- Speed: Fast
- Security: Weak

```python
import hashlib
print(hashlib.sha1(b"Hello, World!").hexdigest())
```

### SHA256
- SHA (Secure Hash Algorithm)
- Bite size: 256
- Output size: 64
- Collision: Yes
- Speed: Fast
- Security: strong

```python
import hashlib
print(hashlib.sha256(b"Hello, World!").hexdigest())
```

### SHA512
- SHA (Secure Hash Algorithm)
- Bite size: 512
- Output size: 128
- Collision: Yes
- Speed: Fast
- Security: stronger

```python
import hashlib
print(hashlib.sha512(b"Hello, World!").hexdigest())
```

### HMAC
- HMAC (Hash-based Message Authentication Code)
- Bite size: 512
- Output size: 128
- Collision: Yes
- Speed: Fast
- Security: strong

```python
import hmac
key = b"secret"
message = b"Hello, World!"
print(hmac.new(key, message, hashlib.sha512).hexdigest())
```


## Mode of Operation

### What is a mode of operation?

A mode of operation is a technique used to encrypt or decrypt a message using a block cipher. A block cipher is an encryption algorithm that encrypts data in fixed-size blocks, typically 64 or 128 bits. A mode of operation describes how to apply the block cipher to encrypt or decrypt a message that is longer than one block.

### what is Block Cipher?

A block cipher is an encryption algorithm that encrypts data in fixed-size blocks, typically 64 or 128 bits. A block cipher takes a fixed-size block of plaintext as input and produces a fixed-size block of ciphertext as output. The same key is used to encrypt and decrypt the data.

### Mode of operation Vs Block Cipher

| Mode of Operation | Block Cipher |
|-------------------|--------------|
| Encrypts/Decrypts a message | Encrypts/Decrypts a block |
| Works on a message of any size | Works on a fixed-size block |
| Uses a block cipher to encrypt/decrypt the message | Uses a key to encrypt/decrypt the block |    

### Common Block Cipher 

- [ECB](#ecb) (Electronic Codebook)
- [CBC](#cbc) (Cipher Block Chaining)
- [PCBC](#pcbc) (Propagating Cipher Block Chaining)
- [CRT](#crt) (Cipher Feedback)


### ECB

- ECB (Electronic Codebook)
- Mode: Block
- Security: Weak
- Speed: Fast
- Description: The simplest mode of operation, where each block of plaintext is encrypted independently.
ryption, you can use the following code:


#### Pros

- Simple and easy to implement.
- Parallelizable: Each block can be encrypted independently.
- Ideal for encrypting small amounts of data.

#### Cons

- Not secure: Identical plaintext blocks will produce identical ciphertext blocks.
- Vulnerable to pattern analysis attacks.


### CBC

- CBC (Cipher Block Chaining)
- Mode: Block
- Security: Strong
- Speed: Slow
- Description: Each block of plaintext is XORed with the previous ciphertext block before encryption.

#### Pros

- confidentiality + Authentication
- Ideal for encrypting large amounts of data.


#### Cons

- Slow: Encryption and decryption are sequential.
- initialization vector (IV) must be known to both the sender and receiver.


### PCBC

- PCBC (Propagating Cipher Block Chaining)
- Mode: Block
- Security: Strong
- Speed: Slow
- Description: Each block of plaintext is XORed with the previous ciphertext block before encryption and the previous plaintext block after encryption.

#### CBC Vs PCBC

| CBC | PCBC |
|-----|------|
| Each block of plaintext is XORed with the previous ciphertext block before encryption. | Each block of plaintext is XORed with the previous ciphertext block before encryption and the previous plaintext block after encryption. |

### CTR

- CTR (Counter)
- Mode: Stream
- Security: Strong
- Speed: Fast
- Description: A block cipher is used to encrypt a counter value, and the resulting ciphertext is XORed with the plaintext to produce the ciphertext.

#### Stream Vs Block Cipher

| Stream Cipher | Block Cipher |
|---------------|--------------|
| Encrypts/Decrypts data one bit at a time. | Encrypts/Decrypts data in fixed-size blocks. |
| Uses a key and an initialization vector (IV) to generate a keystream. | Uses a key to encrypt/decrypt the data. |
| Ideal for encrypting large amounts of data. | Ideal for encrypting small amounts of data. |

#### Pros

- Fast: Encryption and decryption are parallelizable.
- software and hardware implementations are efficient.
- Preprocessing (you are ready with the counter value) 
- Random access: You can encrypt/decrypt any block of data without having to process the entire message.
- Provable security: CTR mode is provably secure if the underlying block cipher is secure.

## Padding Oracle Attack