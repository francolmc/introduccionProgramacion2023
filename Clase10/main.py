# Funcion que muestra el menu con opciones
def menu():
    print('MENU')
    print('1.- sumar')
    print('2.- restar')
    print('3.- multiplicar')
    print('4.- dividir')
    print('5.- salir')
    opcion = int(input('ingrese su opcion: '))
    while not (opcion >= 1 and opcion <= 5): 
        opcion = int(input('Ingrese una opcion correcta: '))
    return opcion

# Funcion que suma dos numeros
def sumar(valor1: int, valor2: int) -> int:
    operacion = valor1 + valor2
    return operacion

# Funcion que resta dos numeros
def restar(valor1: int, valor2: int) -> int:
    operacion = valor1 - valor2
    return operacion

# Funcion que multiplica dos numeros
def multiplicar(valor1: int, valor2: int) -> int:
    operacion = valor1 * valor2
    return operacion

#Funcion que divide dos numeros
def dividir(valor1: int, valor2: int) -> int:
    operacion = valor1 / valor2
    return operacion

opcionMarcada = 0
while opcionMarcada != 5:
    opcionMarcada = menu()
    if opcionMarcada != 5:
        valorUsuario1 = int(input('Ingrese un valor: '))
        valorUsuario2 = int(input('Ingrese otro valor: '))

        if opcionMarcada == 1:
            print('La suma es: ', sumar(valorUsuario1, valorUsuario2))
        elif opcionMarcada == 2:
            print('La resta es: ', restar(valorUsuario1, valorUsuario2))
        elif opcionMarcada == 3:
            print('La multiplicacion es: ', multiplicar(valorUsuario1, valorUsuario2))
        elif opcionMarcada == 4:
            print('La division es: ', dividir(valorUsuario1, valorUsuario2))