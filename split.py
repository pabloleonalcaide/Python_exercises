def devPalabras(fichero):
    cadena = ''
    try:
        f = open(fichero, 'r')
        lista = list(f) 
        cadena = str(lista)        
        f.close()
        lista = cadena.split(',')
        print lista
    except:
        print "algun fallo hubo"
    

devPalabras("fichero2.txt")
