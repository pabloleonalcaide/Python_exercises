class Cancion (object):
	titulo = ""
	autor = ""
	duracion = 0

	def __init__ (self,titulo,autor):
		self.titulo = titulo
		self.autor = autor

	def dame_titulo (self):
		nombre = raw_input("dime el titulo: ")
		self.titulo = nombre
	
	def dame_autor (self):
		autor = raw_input("dime el autor: ")
		self.autor = autor

	def pon_titulo(self, titulo):
		self.titulo=titulo

	def pon_autor (self,autor):
		self.autor=autor

miCancion = Cancion("Cuando zarpa el amor","camela")
print "primera cancion"
print "Titulo: ", miCancion.titulo,", Autor: ", miCancion.autor
print "segunda cancion: "
miCancion.dame_titulo()
miCancion.dame_autor()
print "Titulo: ", miCancion.titulo,", Autor: ", miCancion.autor
print "tercera cancion:"
miCancion.pon_titulo("El torito guapo")
miCancion.pon_autor("El Fary")
print "Titulo: ", miCancion.titulo,", Autor: ", miCancion.autor