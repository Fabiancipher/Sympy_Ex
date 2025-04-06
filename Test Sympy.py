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
print("Este programa encuentra la derivada respecto a x, la integral respecto a x, y el limite cuando x tiende a 0 de una funcion ")
print("EJEMPLO FUNCION: 3x^2 se escribe como 3*x**2")

def derivar(funcion):
    derivada= diff(funcion, x)
    print(derivada)

def integrar(funcion):
    integral= integrate(funcion, x)
    print(integral)

def limite(funcion):
    limite= limit(funcion, x, 0)
    print(limite)
def ayuda():
    print("Un coeficiente a de la variable x se escribe como a*x")
    print("Una potencia n de x se escribe como x**n")
    print("La division se escribe como a/b")
    print("Las funciones se escriben completas sin usar parentesis")
#Da a elegir que desea hacer el usuario
elec= int(input("¿Que desea hacer? \n 1.Derivar \n 2.Integrar \n 3.Encontrar el limite cuando x tiende a 0 \n 4.¡Todas! \n 5. Ayuda \n 6.Salir\n"))
while elec!=6:
    match elec:
        case 1:
           f= input("Ingrese la funcion: ")
           sympificado= sympify(f, locals=locals)
           derivar(sympificado)
           elec= int(input("¿Desea hacer otra cosa?(1-6): "))
        case 2:
           f= input("Ingrese la funcion: ")
           sympificado= sympify(f, locals=locals)
           integrar(sympificado)
           elec= int(input("¿Desea hacer otra cosa?(1-6): "))
        case 3:
           f= input("Ingrese la funcion: ")
           sympificado= sympify(f, locals=locals)
           limite(sympificado)
           elec= int(input("¿Desea hacer otra cosa?(1-6): "))
        case 4:
           f= input("Ingrese la funcion: ")
           sympificado= sympify(f, locals=locals)
           derivar(sympificado)
           integrar(sympificado)
           limite(sympificado)
           elec= int(input("¿Desea hacer otra cosa?(1-6): "))
        case 5:
            ayuda()


