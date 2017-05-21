#-*- coding: utf-8 -*-

# Manejo de una base de datos de libros
# Pablo Leon Alcaide

from Libro import Libro
import MySQLdb


def introducirLibro():
    try:
        mydb = MySQLdb.connect('localhost', 'root', '', 'FONDO_LIBROS')
        libro = Libro(str(raw_input('Un Titulo: ')) , str(raw_input('Un Autor:')), int(raw_input('número paginas:')),int(raw_input('codigo: ')))
        titulo = libro.getTitulo()
        autor = libro.getAutor()
        paginas = libro.getPaginas()
        codigo = libro.getCodigo()
        cursor = mydb.cursor()
        cursor.execute(("INSERT INTO LIBROS VALUES ('%s','%s','%d','%d') ") % (titulo, autor, paginas, codigo))
        cursor.close()
        mydb.commit()
        mydb.close()
    except:
        print 'algo ha fallado en la insercion'


def mostrarCatalogo():
    try:
        mydb = MySQLdb.connect('localhost', 'root', '', 'FONDO_LIBROS')
        cursor = mydb.cursor()
        libros = cursor.execute('SELECT * FROM LIBROS')
        for x in range(libros):
            fila = cursor.fetchone()
            print fila
        cursor.close()
        mydb.commit()
        mydb.close()
    except:
        print "algo ha fallado al intentar mostrar"


def mostrarOrdenados():
    try:
        mydb = MySQLdb.connect('localhost', 'root', '', 'FONDO_LIBROS')
        cursor = mydb.cursor()
        libros = cursor.execute('SELECT * FROM LIBROS order by titulo')
        for x in range(libros):
            fila = cursor.fetchone()
            print fila
        cursor.close()
        mydb.commit()
        mydb.close()
    except:
        print "algo ha fallado al intentar mostrar"


def borrarPorCodigo():
    try:
        mostrarCatalogo()
        idLibro = int(raw_input('indica el indice de libro a eliminar'))
        mydb = MySQLdb.connect('localhost', 'root', '', 'FONDO_LIBROS')
        cursor = mydb.cursor()
        libros = cursor.execute("DELETE FROM LIBROS WHERE codigo ='%s' " % idLibro)
        mydb.commit()
        cursor.close()
        mydb.close()
    except:
        print "algo ha fallado al eliminar"


def mostrarMenu():
    menu = ['Insertar Libro', 'Borrar Libro', 'Mostrar', 'Mostrar Ordenados']
    listaOrdenada = list(enumerate(menu))
    print 'Selecciona una opcion'
    for x in (listaOrdenada):
        print x


def seleccionarOpcion(opcion):
    if opcion == 0:
        introducirLibro()
    elif opcion == 1:
        borrarPorCodigo()
    elif opcion == 2:
        mostrarCatalogo()
    elif opcion == 3:
        mostrarOrdenados():


while True:
    opcion = int(raw_input())
    if opcion > 2:
        break
    mostrarMenu()
    seleccionarOpcion(opcion)
