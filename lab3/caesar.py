# Lab 3 Ceasar Cipher
class Caesar:
    
    def __init__(self, key = 0):
        self.__key = key
        
    def get_key(self):
        return self.__key
    
    def set_key(self, key):
        self.__key = key
        
# I made the encrypt and decrypt methods work for English letters and spcial characters based from the ASCII table values.
    def encrypt(self, plaintext):
        ciphertext = ""
        for char in plaintext:
            if char.isalpha(): 
                shifted = ord(char.lower()) + self.__key
                if shifted > ord('z'):
                    shifted -= 26  
                elif shifted < ord('a'):
                    shifted += 26 
                ciphertext += chr(shifted)
            elif char == ' ': 
                ciphertext += char
            # I encrypted special characters based on the ASCII table values out side of upperand lower case english letters and numbers by using thier ranges
            else:
                shifted = ord(char) + self.__key
                if shifted > 126:
                    shifted = 32 + (shifted - 127) 
                elif shifted < 32:
                    shifted = 127 - (32 - shifted)  
                ciphertext += chr(shifted)
        return ciphertext


    def decrypt(self, ciphertext):
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():  
                shifted = ord(char.lower()) - self.__key
                if shifted < ord('a'):
                    shifted += 26  
                elif shifted > ord('z'):
                    shifted -= 26  
                plaintext += chr(shifted)
            elif char == ' ':  
                plaintext += char
            else:
                shifted = ord(char) - self.__key
                if shifted < 32:
                    shifted = 127 - (32 - shifted) 
                elif shifted > 126:
                    shifted = 32 + (shifted - 127)  
                plaintext += chr(shifted)
        return plaintext

#Testing...

# cipher = Caesar()

# cipher.set_key(3)
# print(cipher.encrypt("hello WORLD!"))  
# print(cipher.decrypt("KHOOR zruog$"))  
# print(cipher.get_key())

# cipher.set_key(6)
# print(cipher.encrypt("zzz"))  
# print(cipher.decrypt("FFF"))
# print(cipher.get_key())  

# cipher.set_key(-6)  
# print(cipher.encrypt("FFF")) 
# print(cipher.get_key()) 

# oneMore = Caesar(5)
# print(oneMore.encrypt("This Was A Pretty Cool Exercise! #$& ***"))
# print(oneMore.decrypt("ymnx bfx f uwjyyd httq jcjwhnxj& ()+ ///"))
