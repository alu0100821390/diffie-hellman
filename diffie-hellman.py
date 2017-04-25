##############################################################
## Universidad de La Laguna						 			##
## Escuela Superior de Ingeniería y Tecnología	 			##
## Grado en Ingeniería Informática				 			##
## Seguridad en Sistemas Informáticos			 			##
## Fecha: 25/04/2017							 			##
## Autor: Kevin Estévez Expósito (alu0100821390) 			##
## 															##
## Práctica 7: Algoritmo de Diffie-Hellman					##
## Descripción: Intercambio de claves de Diffie-Hellman.	##
##											 				##
## Ejecución: py diffie-hellman.py							##
##############################################################


import sys


##### FUNCIONES #####

# Función de exponenciación rápida modular
def exp_rapida(base, exponente, modulo):
	x = 1
	y = base % modulo
	b = exponente
	while (b > 0):
		if ((b % 2) == 0):  # Si b es par...
			y = (y * y) % modulo
			b = b / 2
		else:  # Si b es impar...
			x = (x * y) % modulo
			b = b - 1
	return x

	
##### PROGRAMA PRINCIPAL #####

usu_a = {}  # Diccionario que contendrá los datos necesarios para el usuario A
usu_b = {}  # Diccionario que contendrá los datos necesarios para el usuario B

# Se pide los números p y alpha por teclado
p = int(input("Introduzca el número primo 'p': "))
alpha = int (input("Introduzca el número 'alpha': "))
print ()


# Se pide el secreto xA por teclado
usu_a['x'] = int(input("Usuario A: Introduzca su 'xA' secreto: "))
print ("Usuario A: Calculando 'yA'... ", end = "")
# Se calcula el valor de yA
usu_a['y'] = exp_rapida(alpha, usu_a['x'], p)
print ("'yA' = " + str(usu_a['y']))
print ()


# Se pide el secreto xB por teclado
usu_b['x'] = int(input("Usuario B: Introduzca su 'xB' secreto: "))
print ("Usuario B: Calculando 'yB'... ", end = "")
# se calcula el valor de yB
usu_b['y'] = exp_rapida(alpha, usu_b['x'], p)
print ("'yB' = " + str(usu_b['y']))
print ()


# Se simula el envío de yA al usuario B
print ("Enviando 'yA' al usuario B... ", end = "")
usu_b['y_prim'] = usu_a['y']
print ("Hecho!")

# Se simula el envío de yB al usuario A
print ("Enviando 'yB' al usuario A... ", end = "")
usu_a['y_prim'] = usu_b['y']
print ("Hecho!")
print ()


print ("Usuario A: Generando clave 'k'... ", end = "")
# Se calcula el valor final de la clave para el usuario A
usu_a['k'] = exp_rapida(usu_a['y_prim'], usu_a['x'], p)
print ("'k' = " + str(usu_a['k']))

print ("Usuario B: Generando clave 'k'... ", end = "")
# Se calcula el valor final de la clave para el usuario B
usu_b['k'] = exp_rapida(usu_b['y_prim'], usu_b['x'], p)
print ("'k' = " + str(usu_b['k']))
print ()


# Chivato que comprueba que las claves de los usuarios A y B coinciden
print ()
if (usu_a['k'] == usu_b['k']):
	print ("PERFECTO! Las claves generadas coinciden!")
else:
	print ("ERROR! Las claves generadas NO coinciden!")

sys.exit(0)
