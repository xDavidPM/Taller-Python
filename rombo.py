import sys

filas=int(input('Ingrese dimencion: '))
colum=filas
matriz = []
cont = 0

base = int((filas - 1) / 2)

def llenar_matriz():
    a = 0
    for i in range(filas):
        tmp = []
        for j in range(colum):
            a = ' '
            tmp.append(a)
        matriz.append(tmp)

llenar_matriz()

for i in range(int((filas+1)/2)):
    matriz[base+i][i] = '*'
    matriz[base-i][i] = '*'

    matriz[base+i][(filas-1) - i] = '*'
    matriz[base-i][(filas-1) - i] = '*'

for i in range(filas):
    for j in range(colum):
        sys.stdout.write('{:^5}'.format(matriz[i][j]))
    print ("")

