# Crear un programa en python que solicite 3 valores al usuario y los ordene de mayor a menor,
# pero intercambiando los valores entre variables.
valor1 = int(input('Ingrese un valor: '))
valor2 = int(input('Ingrese otro valor: '))
valor3 = int(input('Ingrese un ultimo valor: '))

aux = 0
if valor1 < valor2:
    aux = valor1
    valor2 = valor1
    valor1 = aux
if valor2 < valor3:
    aux = valor2
    valor3 = valor2
    valor2 = aux
if valor1 < valor2:
    aux = valor1
    valor2 = valor1
    valor1 = aux