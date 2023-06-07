# Crear un programa en python que ingrese dos valores y diga cual es mayor
valor1 = int(input('Ingrese un valor: '))
valor2 = int(input('Ingrese otro valor: '))

if valor1 > valor2:
    print('El primer valor es mayor')
elif valor2 > valor1:
    print('El segundo valor es mayor')
else:
    print('Los valores son iguales')

if valor1 > valor2:
    print('El primer valor es mayor')
else: 
    if valor2 > valor1:
        print('El segundo valor es mayor')
    else:
        print('Los valores son iguales')