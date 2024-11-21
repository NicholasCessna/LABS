# Task 1 Functional Caesar Cipher


def encrypt_char(char,key):
    if char.isalpha():
        shifted = ord(char.lower()) + key
        if shifted > ord('z'):
            shifted -= 26
        elif shifted < ord('a'):
            shifted += 26
        return chr(shifted)
    elif char == ' ':
        return char
    else:
        shifted = ord(char) + key
        if shifted > 126:
            shifted = 32 + (shifted -127)
        elif shifted < 32:
            shifted = 127 - (32 - shifted)
        return chr(shifted)
    
    
def decrypt_char(char, key):
    if char.isalpha():
        shifted = ord(char.lower()) - key
        if shifted < ord ('a'):
            shifted += 26
        elif shifted > ord('z'):
            shifted -= 26
        return chr(shifted)
    elif char == ' ':
        return char
    else:
        shifted = ord(char) - key
        if shifted < 32:
            shifted = 127 - (32 - shifted)
        elif shifted > 126:
            shifted = 32 + (shifted - 127)
        return chr(shifted)
            

    
def encrypt(plaintext, key):
    return ''.join(encrypt_char(char, key) for char in plaintext)
    
def decrypt(ciphertext, key):
    return ''.join(decrypt_char(char, key) for char in ciphertext)
    
    
    
key = 3
plaintext = "This is the text to encode !!#$hhqq"
ciphertext = encrypt(plaintext, key)
print(f"Encrypted: {ciphertext}")
decrypted = decrypt(ciphertext, key)
print(f"Decrypted: {decrypted}") 