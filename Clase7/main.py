# revision del ciclo de repeticion o bucle while
# Realizar un codigo en python que permita realizar la multiplicacion
# de dos valores mediante sumas sucesivas

userValue1 = int(input('Ingrese un valor: '))
userValue2 = int(input('Ingrese otro valor: '))

mult = 0
while userValue1 > 0:
    mult = mult + userValue2
    userValue1 = userValue1 - 1

print('El resultado de la multiplicacion es: ', mult)