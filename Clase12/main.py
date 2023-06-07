# Desarrollar un programa en python que muestre por consola
# los numeros del 1 al 100 incluidos y con un salto de linea
# entre cada print, sustituyendo los siguientes:
# - Multiplos de 3 por la palabra "fizz"
# - Multiplos de 5 por la palabra "buzz"
# - Multiplos de 3 y 5 por la palabra "fizzbuzz"

def esMultiploDeTres(valor: int) -> bool:
    if (valor % 3) == 0:
        return True
    return False

def esMultiploDeCinco(valor: int) -> bool:
    if (valor % 5) == 0:
        return True
    return False

for i in range(100):
    if esMultiploDeTres(i+1) and esMultiploDeCinco(i+1):
        print('fizzbuzz')
    elif esMultiploDeTres(i+1):
        print('fizz')
    elif esMultiploDeCinco(i+1):
        print('buzz')
    else:
        print(i + 1)
