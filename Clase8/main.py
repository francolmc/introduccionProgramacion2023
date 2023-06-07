# Realizar un programa en python que permita al usuario ingresar
# valores mientras el usuario lo desee e infirmar el promedio
# al final.

promedio = 0
suma = 0
respuesta = 's'
contador = 0

while respuesta == 's':
    contador = contador + 1
    valor = int(input('Ingrese un valor: '))
    suma = suma + valor
    respuesta = input('Desea ingresar otro valor? [s/n]: ')

promedio = suma / contador
print('La suma es: ', suma)
print('El promedio es: ', promedio)