# Desarrollar un programa en python que solicite 5 valores al usuario e informe el promedio
suma = 0
for i in range(5):
    valor = int(input('Ingrese un valor: '))
    suma = suma + valor
promedio = suma / 5
print('El promedio es: ', promedio)
if promedio < 4:
    print('El alumno reprobo')
else:
    print('El alumno aprobo')