from cryptography.fernet import Fernet
import random
import string

fileName = None
encryptedFilePath = None
keyFilePath = None
key = None

def generateRandomFileName(): #Generate a new key address
    stringType = string.digits
    randoMString = ( ''.join(random.choice(stringType) for i in range(10)))
    return randoMString

def generateNewKey(fileName : str):
    global key
    key = Fernet.generate_key() #generate a random key
    
    with open(fileName, "r") as f: #Retrive the data
        data = f.read()
    
    encodedData = data.encode()

    masterKey = Fernet(key)

    encryptedData = masterKey.encrypt(encodedData)

    keyFileName = "keys/" + generateRandomFileName() + ".key"

    with open(keyFileName, "wb") as f:
        f.write(key)

    with open(fileName, "wb") as f:
        f.write(encryptedData)

    return keyFileName

def decryptFile(filePath: str, keyPath: str):
    global key
    global encryptedFilePath
    encryptedFilePath = filePath
    with open(filePath, "rb") as f: #Get the encrypted file
        encryptedData = f.read()
    
    with open(keyPath, "rb") as f:
        key = f.read()

    masterKey = Fernet(key)

    try:
        decryptedData = masterKey.decrypt(encryptedData)
        with open(filePath, "w") as f:
            f.write(decryptedData.decode())
    except: return "Error"


def reEncryptTheFile():
    global key
    masterKey = Fernet(key)

    with open(encryptedFilePath, "r") as f:
        data = f.read()

    encryptedData = masterKey.encrypt(data.encode())

    with open(encryptedFilePath, "wb") as f:
        f.write(encryptedData)


