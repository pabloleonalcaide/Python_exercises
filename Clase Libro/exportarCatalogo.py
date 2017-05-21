# -*- coding: utf-8 *-*
import MySQLdb
import webbrowser

def run_query(query=''):
    conn = MySQLdb.connect("localhost", "root", "chapuys", "FONDO_LIBROS")
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


def inicio(cadena=''):
    return '<html><head><title>' + cadena + '</title><style>table {border-collapse: collapse;}</style></head> <body>\n'


def parrafo(texto=''):
    return '<p>' + texto + '</p>\n'


def encabezado( nivel='1', string=''):
    return '<h' + nivel + '>' + string + '</h' + nivel + '>'


def tabla(arreglo):
        temp = '<table border="1"><tr><th>Obra</th><th>Autor</th><th>Paginas</th><th>id</th>\n'
        for renglon in arreglo:
            temp = temp + '<tr>'
            for celda in renglon:
                temp = temp + '<td>' + str(celda) + '</td>\n'
            temp = temp + '</tr>\n'
        return temp + '</table>\n'


def final():
    return '</body> </html>'

f = open('catalogo.html', 'w')
f.write(inicio('Catalogo'))
f.write(encabezado('Catalogo de Libros'))
f.write(parrafo('Libros de la base de datos'))
f.write(tabla(run_query('SELECT * FROM LIBROS')))
f.write(final())
f.close()
webbrowser.open_new_tab('catalogo.html')
