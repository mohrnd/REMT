from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
import binascii

#Run pip install pycryptodomex

def encrypt_AES_GCM(msg, passphrase):
    salt = b'saltysalt' 
    secretKey = PBKDF2(passphrase, salt, dkLen=32)  
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)

def decrypt_AES_GCM(encryptedMsg, passphrase):
    (ciphertext, nonce, authTag) = encryptedMsg
    salt = b'saltysalt'  
    secretKey = PBKDF2(passphrase, salt, dkLen=32) 
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext

passphrase = b'longpassphraselongpassphrase'
print("Passphrase:", passphrase)

msg = b'some random password'
encryptedMsg = encrypt_AES_GCM(msg, passphrase)
print("encryptedMsg", {
    'ciphertext': binascii.hexlify(encryptedMsg[0]),
    'aesIV': binascii.hexlify(encryptedMsg[1]),
    'authTag': binascii.hexlify(encryptedMsg[2])
})

decryptedMsg = decrypt_AES_GCM(encryptedMsg, passphrase)
print("decryptedMsg: ", decryptedMsg)