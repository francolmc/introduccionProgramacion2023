# Crear un programa en python que permita al usuario ingresar 5 valores
# cada valor debe ser almancenado en cada posicion del arreglo.
# Al final del programa se debe informar el promedio del los 5 valores
# El arreglo debe ser definido inicialmente como valores = [0, 0, 0, 0, 0]

valores = [0, 0, 0, 0, 0]

longitud_arreglo = len(valores)
for i in range(longitud_arreglo):
    valores[i] = int(input(f'Ingrese valor {i + 1}: '))

suma = 0
for elemento in valores:
    suma = suma + elemento

promedio = suma / 5
print('Promedio: ', promedio)