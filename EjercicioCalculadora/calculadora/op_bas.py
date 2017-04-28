# -*- coding: utf-8 *-*

#Funcion que suma los dos parametros y devuelve el resultado.
def sumar (num1, num2):
	return num1 + num2

def restar (num1, num2):
#Funcion que resta los dos parametros y devuelve el resultado.
	return num1 - num2

def multiplicar (num1, num2):
#Funcion que multiplica los dos parametros y devuelve el resultado.
	return num1 * num2

def dividir (num1, num2):
#Funcion que divide los dos parametros y devuelve el resultado.
	try:
		resultado = num1 / num2
	except ZeroDivisionError:
		print 'Imposible dividir por cero'
		return -1
	return resultado