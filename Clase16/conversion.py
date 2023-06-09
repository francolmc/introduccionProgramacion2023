# Funcion para convertir unidad a palabra
def unidad_a_palabra(valor: str) -> str:
    unidad = valor[len(valor)-1]
    if unidad == '1': return 'uno'
    elif unidad == '2': return 'dos'
    elif unidad == '3': return 'tres'
    elif unidad == '4': return 'cuatro'
    elif unidad == '5': return 'cinco'
    elif unidad == '6': return 'seis'
    elif unidad == '7': return 'siete'
    elif unidad == '8': return 'ocho'
    elif unidad == '9': return 'nueve'
    return ''

# Funcion para convertir decena a palabra
def decena_a_palabra_old(valor: str) -> str:
    if valor == '10': return 'diez'
    if valor == '11': return 'once'
    if valor == '12': return 'doce'
    if valor == '13': return 'trece'
    if valor == '14': return 'catorce'
    if valor == '15': return 'quince'
    if valor[0] == '1' and int(valor[1]) > 5: return 'dieci'

def decena_a_palabra(valor: str) -> str:
    unidad = valor[len(valor)-1:len(valor)]
    decena = valor[len(valor)-2:len(valor)-1]
    if decena == '1' and unidad == '0': return 'diez'
    if decena == '1' and len(unidad) > 0: return 'dieci'
    # if decena == '1' and unidad == '1': return 'once'
    # if decena == '1' and unidad == '2': return 'doce'
    # if decena == '1' and unidad == '3': return 'trece'
    # if decena == '1' and unidad == '4': return 'catorce'
    # if decena == '1' and unidad == '5': return 'quince'
    # if decena == '1' and unidad == '6': return 'dieciseis'
    # if decena == '1' and unidad == '7': return 'diecisiete'
    # if decena == '1' and unidad == '8': return 'dieciocho'
    # if decena == '1' and unidad == '9': return 'diecinueve'
    if decena == '2' and unidad == '0': return 'veinte'
    if decena == '2' and int(unidad) > 0: return 'veinti'
    if decena == '3': return 'treinta'
    if decena == '4': return 'cuarenta'
    if decena == '5': return 'cincuenta'
    if decena == '6': return 'sesenta'
    if decena == '6': return 'setenta'
    if decena == '9': return 'noventa'
    return ''

def centena_a_palabra(valor: str) -> str:
    centena = valor[len(valor)-3:len(valor)-2]
    decena = valor[len(valor)-2:len(valor)-1]
    if centena == '1' and decena == '0': return 'cien'
    if centena == '1' and len(decena) > 0: return 'ciento'
    if centena == '2': return 'doscientos'
    if centena == '3': return 'trescientos'
    if centena == '4': return 'cuatrocientos'
    if centena == '5': return 'quinietos'
    if centena == '6': return 'seiscientos'
    if centena == '7': return 'setecientos'
    if centena == '8': return 'ochocientos'
    if centena == '9': return 'novecientos'
    return ''

def unidad_de_mil_a_palabras(valor: str) -> str:
    unidad_mil = valor[0]
    if unidad_mil == '1': return 'mil'
    if unidad_mil == '2': return 'dos mil'
    if unidad_mil == '3': return 'tres mil'
    if unidad_mil == '4': return 'cuatro mil'
    if unidad_mil == '5': return 'cinco mil'
    if unidad_mil == '6': return 'seis mil'
    if unidad_mil == '7': return 'siete mil'
    if unidad_mil == '8': return 'ocho mil'
    if unidad_mil == '9': return 'nueve mil'
    return ''
