'''
Created on 20/09/2011

@author: pmartinez
'''
from domain.car import CompactCar

#prueba = domain.MyClass("peugeot", "306", "1999")

print "Ingrese la marca"
tmpMarca = raw_input()
print "Ingrese el modelo"
tmpModelo = raw_input()
print "Ingrese el ano"
tmpAnio = raw_input()

prueba2 = CompactCar(tmpMarca, tmpModelo, tmpAnio)

prueba2.tostring()

