from cryptography.fernet import Fernet

#load ky and cl
file1 = open('ky.txt', 'r')
file2 = open("cl.txt", "r")
ks = file1.readlines()
es = file2.readlines()

print("cls------------------------------")
cont=0;
for line in ks:
    k = ks[cont].strip().encode()
    e = es[cont].strip().encode()

    texto_desencriptado = Fernet(k).decrypt(e).decode()
    print(texto_desencriptado)    
    cont+=1



