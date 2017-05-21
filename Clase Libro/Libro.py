# Clase Libro
# Pablo Leon Alcaide
class Libro(object):

    def __init__(self, titulo, autor, paginas, codigo):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.codigo = codigo

    def setTitulo(self, titulo):
        self.titulo = titulo

    def getTitulo(self):
        return self.titulo

    def setAutor(self, autor):
        self.autor = autor

    def getAutor(self):
        return self.autor

    def setPaginas(self, paginas):
        self.paginas = paginas

    def getPaginas(self):
        return self.paginas

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getCodigo(self):
        return self.codigo

    def __str__(self):
        return 'Libro: '+self.titulo+', Autor: '+self.autor+', num.Paginas: '+self.paginas

