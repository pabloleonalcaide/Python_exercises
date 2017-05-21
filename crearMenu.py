lista = []

# muestra las opciones del menu con el indice al lado
def devolverOpciones(lista):
    listaOrdenada = list(enumerate(lista))
    for x in (listaOrdenada):
        print x

# introduce tantas opciones al menu como el usuario desee
def crearOpciones():
    
    numero = int(raw_input('indica cuantas opciones tiene el menu'))
    for x in range(numero):
        opcion = str(raw_input('introduce opcion'))
        lista.append(opcion)
    return lista

lista = crearOpciones()
devolverOpciones(lista)
