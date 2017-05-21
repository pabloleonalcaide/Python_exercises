conjuntoLetras = map(chr, range(97, 123))

def encriptar(letra):
	auxiliar = 0
	suma = 0
	resultado=0
	if letra == '\n':
		return '\n'
	if letra == ' ':
		return ' '
	if letra >= conjuntoLetras[0] and letra <= conjuntoLetras[len(conjuntoLetras)-1]:
		for x in range(len(conjuntoLetras)):
			if letra == conjuntoLetras[x]:
				suma = auxiliar + 13
				resultado = suma%26
			else:
				auxiliar = auxiliar+1
    	return conjuntoLetras[resultado]

try:
	origen = open('texto.txt', 'r')
	destino = open('textoEncriptado.txt', 'w')
	while True:
		letra = origen.read(1)
	        cifrada = encriptar(letra)
	        if not letra:
	            break
	        destino.write(cifrada)
	origen.close()
	destino.close()
except IOError:
	print "algo ha fallado"


