# Funciones en python

# Funcion sin parametros de entrada
def funcion1():
    print('Hola este es un programa en python')

# Funcion con parametros de entrada
def funcion2(nombre: str):
    print('Hola', nombre, 'este es un programa en python')

# Funcion con retorno de valores
def funcion3(nombre: str) -> str:
    mensaje = 'Hola ' + nombre + ' este es un programa en python'
    return mensaje

# llamar a una funcion si parametros de entrada
funcion1()
# llamar a una funcion con parametros de entrada
funcion2('Pedro')
# llamar a una funcion con parametros de entrada y retorno de valor
print(funcion3('Hector'))