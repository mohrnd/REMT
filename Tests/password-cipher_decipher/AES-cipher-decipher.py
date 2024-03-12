from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
import binascii


def derive_key_from_passphrase(passphrase, key_length=32):
    return PBKDF2(passphrase, b'', dkLen=key_length)

def encrypt_AES_GCM(msg, passphrase):
    secretKey = derive_key_from_passphrase(passphrase)
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)

def decrypt_AES_GCM(encryptedMsg, passphrase):
    (ciphertext, nonce, authTag) = encryptedMsg
    secretKey = derive_key_from_passphrase(passphrase)
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext

passphrase = "your_secret_passphrase" #this can be as long as we want
msg = b'Message for AES-256-GCM + PBKDF2 encryption'

encryptedMsg = encrypt_AES_GCM(msg, passphrase)
print("encryptedMsg", {
    'ciphertext': binascii.hexlify(encryptedMsg[0]),
    'aesIV': binascii.hexlify(encryptedMsg[1]),
    'authTag': binascii.hexlify(encryptedMsg[2])
})

decryptedMsg = decrypt_AES_GCM(encryptedMsg, passphrase)
print("decryptedMsg", decryptedMsg)
