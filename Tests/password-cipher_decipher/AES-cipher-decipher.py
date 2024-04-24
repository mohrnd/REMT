from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
import binascii
import os

def derive_key_from_MasterPassword(MasterPassword, key_length=32):
    return PBKDF2(MasterPassword, b'', dkLen=key_length)

def encrypt_AES_GCM(Password, MasterPassword):
    secretKey = derive_key_from_MasterPassword(MasterPassword)
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(Password.encode('utf-8'))
    return (ciphertext, aesCipher.nonce, authTag)

def decrypt_AES_GCM(encryptedMsg, MasterPassword):
    (ciphertext, nonce, authTag) = encryptedMsg
    secretKey = derive_key_from_MasterPassword(MasterPassword)
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext.decode('utf-8')

def create_password_file(CipheredPassword, aesIV, authTag):
    file_path = 'C:\\ProgramData\\.Vault1851320.txt' 

    with open(file_path, 'a') as file:
        file.write(binascii.hexlify(CipheredPassword).decode('utf-8') + ',' + binascii.hexlify(aesIV).decode('utf-8') + ',' + binascii.hexlify(authTag).decode('utf-8') + '\n')
    try:
        os.system('attrib +H "{}"'.format(file_path))
        print("Password file created successfully.")
    except Exception as e:
        print("Error occurred while setting file attributes:", e)

def add_new_entry(MasterPassword, Password):
    encryptedMsg = encrypt_AES_GCM(Password, MasterPassword)
    print(encryptedMsg)
    create_password_file(*encryptedMsg) # * is used to unpack the elements of a tuple

def get_password(MasterPassword, CipheredPassword):
    try:
        file_path = 'C:\\ProgramData\\.Vault1851320.txt'
        with open(file_path, 'r') as file:
            lines = file.readlines()
        for line in lines:
            components = line.strip().split(',')
            if CipheredPassword == components[0]:
                encrypted_password = binascii.unhexlify(components[0])
                aesIV = binascii.unhexlify(components[1])
                authTag = binascii.unhexlify(components[2])
                decrypted_password = decrypt_AES_GCM((encrypted_password, aesIV, authTag), MasterPassword)
                return decrypted_password
            
        print("CipheredPassword not found in the file.")
        return None
    except Exception as e:
        print("Error occurred while getting password:", e)
        return None



# Usage 
# print(add_new_entry('MASTERPASSWORD', 'Pa$$w0rd6')) 
# print(get_password('MASTERPASSWORD','c068a006d333f05307'))