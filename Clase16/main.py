from conversion import unidad_a_palabra
from conversion import decena_a_palabra
from conversion import centena_a_palabra
from conversion import unidad_de_mil_a_palabras

def esUnValorValido(valor: int) -> bool:
    if valor <= 0 or valor > 9999:
        return False
    return True

valor = input('Ingrese valor: ')
while not esUnValorValido(int(valor)):
    print('Ingrese valores entre 1 y 9999')
    valor = input('Ingrese nuevamente un valor: ')

# cantidad_letras = len(valor)
# print(valor[cantidad_letras-2:cantidad_letras])
palabra = ''
if len(valor) >= 4: 
    palabra = palabra + ' ' + unidad_de_mil_a_palabras(valor)
if len(valor) >= 3:
    palabra = palabra + ' ' + centena_a_palabra(valor)
if len(valor) >= 2: 
    palabra = palabra + ' ' + decena_a_palabra(valor)
if int(valor) > 0 and (int(valor) < 10 or int(valor) > 19):
    if int(valor) > 29:
        palabra = palabra + ' y '
    palabra = palabra + unidad_a_palabra(valor)
# if cantidad_letras >= 2:
#     palabra = decena_a_palabra(valor[cantidad_letras-2:cantidad_letras])
# if valor[cantidad_letras - 1] != '0':
#     palabra = palabra + unidad_a_palabra(valor[cantidad_letras - 1])
# 
# print(palabra)

# print(valor[len(valor)-1:len(valor)])
# print(valor[len(valor)-2:len(valor)-1])

print(palabra)
