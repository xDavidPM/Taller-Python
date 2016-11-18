from random import randint
import sys
import random

matriz = []
x=0
y=0
direccion = ""
enProgreso = True
filas = 10#int(raw_input("Cantidad de Filas: "))
columnas = 10#int(raw_input("Cantidad de Columnas: "))
playerHP = 0
playerAgilidad = 25
turnos = 0
global numEnemigos
numEnemigos = 0

def llenarMatriz():
	a=0
	for i in range(filas):
		tmp = []
		for j in range(columnas):
			#elemento = "%d,%d" % (i,j)
			a += 1
			tmp.append(a)
		matriz.append(tmp)

def reiniciarJuego():
	a=0
	global x
	global y
	x = 0
	y = 0
	global playerHP
	global playerAgilidad
	for i in range(filas):
		for j in range(columnas):
			a += 1
			matriz[i][j] = a

def hayMonstruo():
	hay = False
	a = random.randrange(100)+1
	if a <= 40:
		hay = True
	return hay


llenarMatriz()


while enProgreso:
	#Dibujar Matriz
	matriz[x][y] = 0
	for i in range(filas):
		
		for j in range(columnas):
			#elemento = "%d,%d" % (i,j)
			#sys.stdout.write(str(matriz[i][j]))
			sys.stdout.write('{:^5}'.format(matriz[i][j]))
		print ("\n")
	#Elijo la direccion
	direccion = ""
	while direccion != "e" and direccion != "o" and direccion != "n" and direccion != "s":
		direccion = input("Elija una direccion [n], [s], [e], [o]: ")
	print ("")

	if direccion == 's':
		if x + 1 < filas:
			x += 1
			matriz[x][y] = 0
		else:
			print("Usted esta en el limite Sur, no puede ir mas al Sur.")

	if direccion == 'n':
		if x - 1 > 0:
			x -= 1
			matriz[x][y] = 0
		else:
			print("Usted esta en el limite Norte, no puede ir mas al Norte.")

	if direccion == 'e':
		if y + 1 < columnas:
			y += 1
			matriz[x][y] = 0
		else:
			print("Usted esta en el limite Este, no puede ir mas al Este.")

	if direccion == 'o':
		if y - 1 > 0:
			y -= 1
			matriz[x][y] = 0
		else:
			print("Usted esta en el limite Oeste, no puede ir mas al Oeste.")

	print ("Usted esta en la casilla: (",x+1," , ", y+1,")")

	turnos += 1

	if hayMonstruo():
		print ("\n  ¡¡¡UN MOSTRUO!!!  \n")
		numEnemigos += 1

	if direccion == 'salir':
		enProgreso = False
		
	if x == (filas-1) and y == (columnas - 1):
		print ("FELICIDADES, Encontraste el tesoro")
		print ("Turnos: ", turnos)
		print ("Numero de Enemigos: ", numEnemigos)
		enProgreso = False


