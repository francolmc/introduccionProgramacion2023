# Funcion para convertir unidad a palabra
def unidad_a_palabra(valor: str) -> str:
    if valor == '1': return 'uno'
    elif valor == '2': return 'dos'
    elif valor == '3': return 'tres'
    elif valor == '4': return 'cuatro'
    elif valor == '5': return 'cinco'
    elif valor == '6': return 'seis'
    elif valor == '7': return 'siete'
    elif valor == '8': return 'ocho'
    elif valor == '9': return 'nueve'

# Funcion para convertir decena a palabra
def decena_a_palabra(valor: str) -> str:
    if valor == '10': return 'diez'
    if valor == '11': return 'once'
    if valor == '12': return 'doce'
    if valor == '13': return 'trece'
    if valor == '14': return 'catorce'
    if valor == '15': return 'quince'
    if valor[0] == '1' and int(valor[1]) > 5: return 'dieci'