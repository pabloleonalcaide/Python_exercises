class Empleado (object):

	def __init__(self):
		self.nif = 12345678
		self.s_base = 1000
		self.saldo_hExtra = 10
		self.horas_extras = 5
		self.irpf = 1
		self.casado = True
		self.hijos = 0

	def calcularComplemento(self):
		return self.saldo_hExtra*self.horas_extras

	def calcularSueldoBruto(self):
		bruto = self.calcularComplemento() + self.s_base
		return bruto

	def devolverRetenciones(self):
		porcentaje =0.16
		if self.casado == True:
			porcentaje= porcentaje-0.02
		if self.hijos >0:
			desgrava = 0.01* self.hijos
			porcentaje = porcentaje -desgrava
			
		retencion =  porcentaje* self.calcularSueldoBruto()
		return retencion

	def calcularSueldoNeto(self):
		return ( self.calcularSueldoBruto() - self.devolverRetenciones())

	def mostrarInformacion(self):
		print '     DATOS ECONOMICOS --> '
		print 'sueldo base: ',self.s_base
		print 'complementos: ',self.calcularComplemento()
		print 'sueldo bruto: ',self.calcularSueldoBruto()
		print 'retenciones: ',self.devolverRetenciones()
		print 'sueldo neto ', self.calcularSueldoNeto()

	def imprimeTodo(self):
		print '     DATOS GENERALES --> '
		print 'sueldo base: ',self.s_base
		print 'nif: ', self.nif
		if self.casado == True:
			print 'Estado: casado'
		else: 
			print 'Estado: soltero'
		print 'hijos: ', self.hijos
		print 'complementos: ',self.calcularComplemento()
		print 'sueldo bruto: ',self.calcularSueldoBruto()
		print 'retenciones: ',self.devolverRetenciones()
		print 'sueldo neto ', self.calcularSueldoNeto()		

empleado = Empleado()
empleado.mostrarInformacion()
print ''
empleado.imprimeTodo()