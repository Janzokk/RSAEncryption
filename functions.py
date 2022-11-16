from cryptography.fernet import Fernet

#genera una clau i la guarda en un fitxer
def key_generator():
    key = Fernet.generate_key()

    with open("key.txt", "wb") as file:
        file.write(key)

#obte una clau generada previament
def get_key():
    with open("key.txt", "rb") as file:
        key = file.read()

    return key

#xifrar text     

def encrypt(text, key):
    f = Fernet(key)
    code = f.encrypt(text.encode())

    return code

#desxifrar text
def desencrypt(text, key):
    f = Fernet(key)
    decrypted = f.decrypt(text).decode()
    
    return decrypted