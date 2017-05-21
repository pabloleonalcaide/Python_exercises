# -*- coding: utf-8 *-*
import MySQLdb

def run_query(query=''):
 
 conn = MySQLdb.connect("localhost","root","","pruebaPython") # Conectar a la base de datos
 cursor = conn.cursor() # Crear un cursor
 cursor.execute(query) # Ejecutar una consulta
 if query.upper().startswith('SELECT'):
 	data = cursor.fetchall() # Traer los resultados de un select
 else:
 	conn.commit() # Hacer efectiva la escritura de datos
 	data = None
 cursor.close() # Cerrar el cursor
 conn.close() # Cerrar la conexión
 return data

def inicio( cadena='' ):
      return '''<html><head><title>''' + cadena + '''</title></head> <body>\n'''
def parrafo(texto='' ):
    return '<p>' + texto + '</p>\n'

def encabezado( nivel='1',  string='' ):
    return '<h'+ nivel + '>'+ string + '</h'+ nivel + '>'
def tabla( arreglo ):
        temp =  '<table border="1">\n'

        for renglon in arreglo:
            temp = temp + '<tr>'
            for celda in renglon:
                temp = temp + '<td>' + str(celda) + '</td>\n'
            temp = temp + '</tr>\n'
        return temp + '</table>\n'

def final():
    return '''</body> </html>'''    
f = open('superheroes.html','w')
f.write(inicio('Tabla Superheroes'))
f.write(encabezado('Tabla de Superheroes'))
f.write(parrafo('Superheroes ordenados por nombre de superheroe'))
f.write(tabla(run_query('SELECT * FROM SUPERHEROES ORDER BY superheroe')))
f.write(parrafo('Superheroes ordenados por nombre de identidad secreta'))
f.write(tabla(run_query('SELECT * FROM SUPERHEROES ORDER BY identidad_secreta')))
f.write(final())
f.close()
