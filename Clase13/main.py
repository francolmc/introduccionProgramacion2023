# Alcance de las variables
valorGlobal = 0

def incrementarUno():
    # valorIncrementoUno es una variable local
    # con alcance solo dentro de la funcion
    valorIncrementoUno = 1
    global valorGlobal
    valorGlobal = valorGlobal + 1

def incrementarN(n: int):
    # la palabra reservada global permite indicar que una varible dentro de la
    # funcion sera accedida fuera de la funcion.
    global valorGlobal
    valorGlobal = valorGlobal + n

incrementarUno()
print(valorGlobal)
incrementarUno()
print(valorGlobal)
incrementarN(3)
print(valorGlobal)
incrementarUno()
print(valorGlobal)
# print(valorIncrementoUno)
