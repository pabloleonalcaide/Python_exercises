#Pablo Leon Alcaide
#Give me three different numbers, i'll print a number stair with them! fun!
lista = []

print "ESCALERA DE NUMEROS"
valor1 = int(raw_input("Escriba el primer numero"))
valor2 = int(raw_input("Escriba el segundo numero"))
valor3 = int(raw_input("Escriba el tercer numero"))
if valor1 == valor2 or valor2 == valor3:
	print "no ha escrito numeros validos!"
else:
	if valor1 < valor2:
		for a in reversed (range((valor1), (valor2+1))):
			lista.append(a)	
	else:
		for b in reversed (range((valor2), (valor1+1))):
			lista.append(b)	
	
	if valor2 < valor3:
		for c in range ((valor2+1),(valor3+1)):
			lista.append(c)
	else:
		for d in range ((valor3+1),(valor2+1)):
			lista.append(d)
	print lista
