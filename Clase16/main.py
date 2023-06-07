from conversion import unidad_a_palabra
from conversion import decena_a_palabra

def esUnValorValido(valor: int) -> bool:
    if valor <= 0 or valor > 9999:
        return False
    return True

valor = input('Ingrese valor: ')
while not esUnValorValido(int(valor)):
    print('Ingrese valores entre 1 y 9999')
    valor = input('Ingrese nuevamente un valor: ')

cantidad_letras = len(valor)
print(valor[cantidad_letras-2:cantidad_letras])
palabra = ''
if cantidad_letras >= 2:
    palabra = decena_a_palabra(valor[cantidad_letras-2:cantidad_letras])
if valor[cantidad_letras - 1] != '0':
    palabra = palabra + unidad_a_palabra(valor[cantidad_letras - 1])

print(palabra)