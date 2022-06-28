from cryptography.fernet import Fernet

#load cls
file1 = open('cls.txt', 'r')
cls = file1.readlines()
ks=[]
es=[]

for line in cls:
    key = Fernet.generate_key()
    ks.append(key.decode())
    objeto_cifrado = Fernet(key)

    texto_encriptado = objeto_cifrado.encrypt((line.strip()).encode())
    es.append(texto_encriptado.decode())

print("ky----------------------------")
for line1 in ks:
    print(line1)

print("cl----------------------------")
for line2 in es:
    print(line2)




