from cryptography.fernet import Fernet

def key_generator():
    key = Fernet.generate_key()

    with open("key.txt", "w") as file:
        file.write(key)

def get_key():
    with open("key.txt", "r") as file:
        key = file.read()

    return key

#cifrar los documentos     

def encrypt(text, key):
    f = Fernet(key)
    code = f.encrypt('b', text)

    return code

def desencrypt(text, key):
    f = Fernet(key),
    decrypted = f.decrypt('b', text)
    
    return decrypted