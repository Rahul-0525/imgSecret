# link for reference to learn about this code: https://gemini.google.com/share/153bee9247ba

import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import base64


class security():
    """provide the methods for encryptmsg and decryptmsg child classes"""

    def __init__(self):
        """Do nothing"""
        pass
        
    def generateSalt(self) -> str:
        """generate and return a new 16 raw byte salt value for each image during encryption"""
        salt = os.urandom(16) 
        return salt

    def setMasterPwd(self) -> str:
        """ask user for master password as input and return the byte encoded str"""
        master = input("Enter the Master Password: ")   
        return master.encode('utf-8')   

    def generateKey(self, mpwd, salt) -> str:
        """use the salt and masterPwd attribute stored in self to generate and return the key for encryption and decryption"""
        master_password = mpwd
        seed_salt = salt

        keyDerivative = PBKDF2HMAC(algorithm=hashes.SHA256(),
                        length=32,
                        salt=seed_salt,
                        iterations=60000)

        key = keyDerivative.derive(master_password)
        return key
        


class encryptMsg(security):

    def __init__(self, msg:str) -> str:
        """
        argument: message to encrypt

        sets up the key using salt and master password for encryption
        and call encrypt function to encrypt the message in one go"""
        self.msg = msg
        self.masterPwd = self.setMasterPwd()
        self.salt = self.generateSalt()
        self.key = self.generateKey(self.masterPwd,self.salt)
        self.encryptedmsg = self.encrypt()

    def encrypt(self) -> str:
        """
        argument: nothing
        encrypts the message object and returns the encrypted str ready to be stored in the image"""

        msg = self.msg
        message = msg.encode('utf-8')

        aesengine =AESGCM(self.key)
        nonce = os.urandom(12)
        ciphertext = aesengine.encrypt(nonce,message, None)

        ciphertext_b64str = base64.b64encode(ciphertext).decode('utf-8')
        salt_b64str = base64.b64encode(self.salt).decode('utf-8')
        nonce_b64str = base64.b64encode(nonce).decode('utf-8')
        return "001as".join([salt_b64str, nonce_b64str, ciphertext_b64str])
    
    def getEncMsg(self) -> str:
        """returns the encrypted message"""
        return self.encryptedmsg

class decryptMsg(security):

    def __init__(self, extracted:str) -> str:
        """
        argument: encrypted msg 
        extracts the salt, nonce and ciphertext from the str extracted from the image and set up the key for decryption
        
        and call decrypt function"""

        elementlst = extracted.split("001as")
        salt_b64str = elementlst[0]
        nonce_b64str = elementlst[1]
        ciphertext_b64str = elementlst[2]

        self.salt = base64.b64decode(salt_b64str)
        self.nonce = base64.b64decode(nonce_b64str)
        self.ciphertext = base64.b64decode(ciphertext_b64str)
        self.masterPwd = self.setMasterPwd()
        self.key = self.generateKey(self.masterPwd,self.salt)

        self.decryptedmsg = self.decrypt()

    def decrypt(self) -> str:
        """
        argument: nothing
        decrypts and return the decrypted message finally"""

        aesengine = AESGCM(self.key)

        decrypted_msg = aesengine.decrypt(self.nonce, self.ciphertext, None)
        msg = decrypted_msg.decode('utf-8')

        return msg
    
    def getDecrMsg(self) -> str:
        """returns the decrypted message"""
        return self.decryptedmsg


# enc = encryptMsg("hello is it working")
# print(enc.getEncMsg())

# dec = decryptMsg(enc.getEncMsg())
# print(dec.getDecrMsg())


        
    


    


