import fileinput
import math

lines = []
for line in fileinput.input():
    lines.append(line.upper())
tableau = {
            'E': [0,0], 'N': [0,1], 'C': [0,2], 'R': [0,3], 'Y': [0,4],
            'P': [1,0], 'T': [1,1], 'A': [1,2], 'B': [1,3], 'D': [1,4],
            'F': [2,0], 'G': [2,1], 'H': [2,2], 'I': [2,3], 'K': [2,4],
            'L': [3,0], 'M': [3,1], 'O': [3,2], 'Q': [3,3], 'S': [3,4],
            'U': [4,0], 'V': [4,1], 'W': [4,2], 'X': [4,3], 'Z': [4,4]
}

fila = []
fila2 = []
mensaje = ''
if lines[0]=="ENCRYPT\n":
    for j in range(len(lines[1])):
        for n in tableau:
            if lines[1][j] == n:
                fila.append(tableau[n])
    if len(fila) % 2 != 0:
        for i in range(2):
            for j in range(0,len(fila)-1,2):
                if i == 0: 
                    fila2.append([fila[j][i],fila[j+1][i]])
                    if j == 14 :
                        fila2.append([fila[16][i+1],fila[0][i+1]])
                else: 
                    fila2.append([fila[j+1][i],fila[j+2][i]])
    else: 
        for i in range(2):
            for j in range(0,len(fila)-1,2):
                fila2.append([fila[j][i],fila[j+1][i]])

    for i in fila2:
        for j in tableau:
            if i == tableau[j]:
                mensaje+=(j)
    print (mensaje)
else:
    for j in range(len(lines[1])):
        for n in tableau:
            if lines[1][j] == n:
                fila.append(tableau[n])
    x= len(fila)/2 
    x= math.floor(x)
    if len(fila) % 2 == 0:
        for j in range(0,int(len(fila)/2),1):
            for i in range(2):
                fila2.append([fila[j][i],fila[x][i]])
            x=x+1
    else:
        for j in range(0,x+1,1):
            for i in range(2):
                if i == 0:
                    fila2.append([fila[j][i],fila[x][i+1]])
                else:
                    if x < len(fila)-1:
                        x=x+1
                    if j<8 and i==1:
                        fila2.append([fila[j][i],fila[x][i-1]])
    for i in fila2:
        for j in tableau:
            if i == tableau[j]:
                mensaje+=(j)
    print (mensaje)