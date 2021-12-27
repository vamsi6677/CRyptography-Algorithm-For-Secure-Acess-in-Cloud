import secrets
import random
import sys
from Cryptodome.Cipher import AES 
from Cryptodome import Random   
import hybrid

pri=input("Enter the Private Key: ")
cipherKey=input("Enter the AES Symmetric Key: ")
cipherText=input("Enter cipher text: ")
print(pri)
decriptedKey=''.join(hybrid.decrypt(pri,cipherKey))
decriptedKey=''.join(hybrid.decrypt(cipherKey))
print()
print("Decrypting the AES Symmetric Key...")

decriptedKey=decriptedKey.encode('utf-8')
cipherAESd = AES.new(decriptedKey, AES.MODE_GCM, nonce=nonce)
decrypted=hybrid.decryptAES(cipherAESd,cipherText)
print()
print("Decrypting the message using the AES symmetric key.....")
print("decrypted message: ", decrypted)
