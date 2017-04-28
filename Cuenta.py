class Cuenta (object):
    def __init__ (self):
        self.saldo = 0

    # otra posibilidad de constructor    
#    def __init__ (self, cantidad = 0):
#        self.saldo = cantidad
        
    def ingresar (self, cantidad):
        self.saldo += cantidad
    
    def retirar (self, cantidad):
        self.saldo -= cantidad
        


cuenta = Cuenta()
print 'Cuenta recien creada: saldo = ', cuenta.saldo
ingresos = [125.23, 503.4, 50]
for i in ingresos:
    cuenta.ingresar(i)
    print 'Ingreso nuevo: saldo = ', cuenta.saldo 
    cuenta.retirar(333.34)
    print 'Retirada de efectivo: saldo = ', cuenta.saldo