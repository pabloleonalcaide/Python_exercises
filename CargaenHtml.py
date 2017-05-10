# -*- coding: utf-8 *-*
import MySQLdb

def run_query(query=''):
 
 conn = MySQLdb.connect("localhost","root","bd130","superheroes")
 cursor = conn.cursor() 
 cursor.execute(query) 
 if query.upper().startswith('SELECT'):
 	data = cursor.fetchall() 
 else:
 	conn.commit() 
 	data = None
 cursor.close() 
 conn.close() 
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
f = open('listaSuperheroes.html','w')
f.write(inicio('Superheroes'))
f.write(encabezado('Superheroes e Identidades'))
f.write(parrafo('Lista de Superheroes ordenados por Alias'))
f.write(tabla(run_query('SELECT * FROM SUPERHEROES ORDER BY superheroe')))
f.write(parrafo('Lista de Superheroes ordenados por su identidad secreta'))
f.write(tabla(run_query('SELECT * FROM SUPERHEROES ORDER BY identidad_secreta')))
f.write(final())
f.close()