# -*- coding: utf-8 -*-
"""
Ejemplo Sympy
Hector Fabian Cabrera Vargas
"""
#Importa toda la libreria
from sympy import *
#Define x como un simnolo valido de operacion
x= Symbol('x')
#Lo define como un local
locals= {'x':x}
f= input("Ingrese la funcion: ")
#Sympify convierte lo ingresado en algo que puede entender sympy. Lo define como un simbolo
sympificado= sympify(f, locals=locals)

def derivar(funcion):
    derivada= diff(funcion, x)
    print(derivada)

def integrar(funcion):
    integral= integrate(funcion, x)
    print(integral)

def limite(funcion):
    limite= limit(funcion, x, 0)
    print(limite)
#Da a elegir que desea hacer el usuario
elec= int(input("¿Que desea hacer? \n 1.Derivar \n 2.Integrar \n 3.Encontrar el limite cuando x tiende a 0 \n 4.¡Todas! \n"))
match elec:
    case 1:
       derivar(sympificado)
    case 2:
       integrar(sympificado)
    case 3:
       limite(sympificado)
    case 4:
       derivar(sympificado)
       integrar(sympificado)
       limite(sympificado)


