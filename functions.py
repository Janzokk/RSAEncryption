import rsa

#genera una clau i la guarda en un fitxer
def key_generator():
    (pkey, skey) = rsa.newkeys(1024)

    with open("public_key.txt", "wb") as file:
        file.write(pkey.save_pkcs1('PEM'))
    with open("secret_key.txt", "wb") as file:
        file.write(skey.save_pkcs1('PEM'))

#obte una clau generada previament
def get_key():
    with open('public_key.txt', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('secret_key.txt', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())

    return privateKey, publicKey

#xifrar text     
def encrypt(text, key):
    return rsa.encrypt(text.encode('ascii'), key)

#desxifrar text
def desencrypt(text, key):
    return rsa.decrypt(text, key).decode('ascii')