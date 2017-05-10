def cifrarLetra(self,letra):
	cifrada = (char)((letra+13)%26)
	return cifrada
fichero = open ('textoInicio.txt','w');
ficheroEncriptado = open('textoEncriptado')

while True:
    letra = fichero.read(1)
    if not letra:
        print "End of file"
        break
    letraModificada= encriptarLetra(letra)
    ficheroEncriptado.write(letraModificada)

fichero.close()

