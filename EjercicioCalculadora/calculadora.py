# -*- coding: utf-8 *-*

from calculadora import op_bas

opcion = 5
valor1 = int(raw_input("indica el primer valor "))
valor2 = int(raw_input("indica el segundo valor "))
print '1-Sumar'
print '2-Restar'
print '3-Multiplicar'
print '4-Dividir'
while opcion <> 0:
	opcion = int(raw_input("escoge una opcion, cero para salir"))
	if opcion == 0:
		print "adios"
	elif opcion == 1:
		print "resultado",op_bas.sumar(valor1,valor2)
	elif opcion == 2:
		print "resultado",op_bas.restar(valor1,valor2)
	elif opcion == 3:
		print "resultado",op_bas.multiplicar(valor1,valor2)
	elif opcion == 4:
		print "resultado",op_bas.dividir(valor1,valor2)	
	else:
		print "escoge una opcion correcta"
