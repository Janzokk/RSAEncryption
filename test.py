import functions;

op = input("What do you want to do:\n1.Generate key\n2.Get key\n3.Encrypt text\n4.Decrypt text\n")
(pkey, skey) = functions.get_key()

if(op == '1'):
    functions.key_generator()
    print("Key file created") 
elif(op == '2'):
    (pkey, skey) = functions.get_key()
    print(pkey)
    print(skey)
elif(op == '3'):
    text = input("Enter the text you want to encrypt: ")
    
    print(functions.encrypt(text, skey))
elif(op == '4'):
    text = input("Enter the text you want to decrypt: ")
    print(functions.desencrypt(text, pkey))