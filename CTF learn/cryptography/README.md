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