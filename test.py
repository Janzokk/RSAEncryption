import functions;

op = input("What do you want to do:\n1.Generate key\n2.Get key\n3.Encrypt text\n4.Decrypt text\n")

if(op == '1'):
    functions.key_generator()
    print("Key file created") 
elif(op == '2'):
    key = functions.get_key()
    print(b"Your key is: "+key)
elif(op == '3'):
    text = input("Enter the text you want to encrypt: ")
    print(functions.encrypt(text, functions.get_key()))
elif(op == '4'):
    text = input("Enter the text you want to decrypt: ")
    print(functions.desencrypt(text, functions.get_key()))