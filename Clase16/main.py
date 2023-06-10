from conversion import unidad_a_palabra
from conversion import decena_a_palabra
from conversion import centena_a_palabra
from conversion import unidad_de_mil_a_palabra

def esUnValorValido(valor: int) -> bool:
    if valor <= 0 or valor > 9999:
        return False
    return True

valor = input('Ingrese valor: ')
while not esUnValorValido(int(valor)):
    print('Ingrese valores entre 1 y 9999')
    valor = input('Ingrese nuevamente un valor: ')

palabra = ''
if len(valor) >= 4:
    palabra = palabra + unidad_de_mil_a_palabra(valor)
if len(valor) >= 3:
    palabra = palabra + ' ' + centena_a_palabra(valor)
if len(valor) >= 2:
    palabra = palabra + ' ' + decena_a_palabra(valor)
if len(valor) >= 1 and valor[len(valor) - 1] != '0': 
    if int(valor) > 29:
        palabra = palabra + ' y'
    palabra = palabra + ' ' + unidad_a_palabra(valor)

print(palabra)