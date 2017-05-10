arrayLetras = map(chr, range(97, 123))

def encriptar(letra):
	auxiliar = 0
	suma = 0
	resultado=0
	if letra == '\n':
		return '\n'
	if letra >= arrayLetras[0] and letra <= arrayLetras[len(arrayLetras)-1]:
		for x in range(len(arrayLetras)):
			if letra == arrayLetras[x]:
				suma = auxiliar + 13
				resultado = suma%26
			else:
				auxiliar = auxiliar+1
    	return arrayLetras[resultado]


origen = 'textoInicio.txt'
destino = 'textoFin.txt'

ficheroOrigen = open(origen, 'r')
ficheroDestino = open(destino, 'w')

while True:
    letra = ficheroOrigen.read(1)

    cifrada = cifrarLetra(letra)
    if not letra:
        break

    ficheroDestino.write(letraCifrada)
ficheroOrigen.close()
ficheroDestino.close()