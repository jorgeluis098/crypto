import fileinput
import math
from operator import xor # para poder realizar la operacion xor

# lines = []
# for line in fileinput.input():
#     lines.append(line)

#algoritmo KSA
S=[]
T=[]
keyStream=[]
mensaje=[] 
n=0
j=0
key="Clave de 128 bit"
#Se llena el vector S con numeros  0-255 y T con la key
for i in range(256):
    if n== len(key):
        n=0
    S.append(i)
    T.append(key[n])
    n=n+1
for i in range(256):
    j= ((j + S[i] + ord(T[i])) % 256 ) 
    #SWAP con variable temporal
    temp = S[i]
    S[i] = S[j] 
    S[j] = temp
#PRGA
j=0
entrada="Un saludo"
for i in range(1,len(entrada)+1):
    j=((j + S[i]) % 256)
    temp = S[i]
    S[i] = S[j] 
    S[j] = temp
    keyStream.append(S[(S[i]+S[j]) % 256])
    mensaje.append(hex(xor(keyStream[i-1],ord(entrada[i-1])))) # xor y se convierte a hex
print (mensaje)