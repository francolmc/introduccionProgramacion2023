# Crear un programa en python que permita al usuario ingresar 5 valores
# cada valor debe ser almancenado en cada posicion del arreglo.
# Al final del programa se debe informar el promedio del los 5 valores

# Definicion de un arreglo vacio
valores = []

# Esto es una constante, ya que no cambia su valor a lo largo del programa
CANTIDAD_VALORES = 5

for i in range(CANTIDAD_VALORES):
    valor = float(input(f'Ingrese el valor {i + 1} de {CANTIDAD_VALORES}: '))
    # append nos permite agregar elementos al arreglo
    valores.append(valor)

suma = 0
for elemento in valores:
    suma = suma + elemento

promedio = suma / CANTIDAD_VALORES
print('Promedio: ', promedio)