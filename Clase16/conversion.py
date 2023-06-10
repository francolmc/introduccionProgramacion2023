# Funcion para convertir unidad a palabra
def unidad_a_palabra(valor: str) -> str:
    unidad = valor[len(valor) - 1]
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
def decena_a_palabra(valor: str) -> str:
    unidad = valor[len(valor) - 1]
    decena = valor[len(valor) - 2]
    if decena == '1' and unidad == '0': return 'diez'
    if decena == '1' and unidad == '1': return 'once'
    if decena == '1' and unidad == '2': return 'doce'
    if decena == '1' and unidad == '3': return 'trece'
    if decena == '1' and unidad == '4': return 'catorce'
    if decena == '1' and unidad == '5': return 'quince'
    if decena == '1' and unidad == '6': return 'dieciseis'
    if decena == '1' and unidad == '7': return 'diecisiete'
    if decena == '1' and unidad == '8': return 'dieciocho'
    if decena == '1' and unidad == '9': return 'diecinueve'
    if decena == '2' and unidad == '0': return 'veinte'
    if decena == '2' and int(unidad) >= 0: return 'veinti'
    if decena == '3': return 'treinta'
    if decena == '4': return 'cuarenta'
    if decena == '5': return 'cincuenta'
    if decena == '6': return 'sesenta'
    if decena == '7': return 'setenta'
    if decena == '8': return 'ochenta'
    if decena == '9': return 'noventa'
    return ''

# Funcion para convertir centena a palabra
def centena_a_palabra(valor: str) -> str:
    unidad = valor[len(valor) - 1]
    decena = valor[len(valor) - 2]
    centena = valor[len(valor) - 3]
    if centena == '1' and (len(decena) > 0 or len(unidad) > 0): return 'ciento'
    elif centena == '1' and decena == '0' and unidad == '0': return 'cien'
    if centena == '2': return 'doscientos'
    if centena == '3': return 'trescientos'
    if centena == '4': return 'cuatrocientos'
    if centena == '5': return 'quinientos'
    if centena == '6': return 'seiscientos'
    if centena == '7': return 'setecientos'
    if centena == '8': return 'ochocientos'
    if centena == '9': return 'novecientos'
    return ''

# Funcion para convertir unidad de mil a palabras
def unidad_de_mil_a_palabra(valor: str) -> str:
    unidad_de_mil = valor[0]
    if unidad_de_mil == '1': return 'mil'
    if unidad_de_mil == '2': return 'dos mil'
    if unidad_de_mil == '3': return 'tres mil'
    if unidad_de_mil == '4': return 'cuatro mil'
    if unidad_de_mil == '5': return 'cinco mil'
    if unidad_de_mil == '6': return 'seis mil'
    if unidad_de_mil == '7': return 'siete mil'
    if unidad_de_mil == '8': return 'ocho mil'
    if unidad_de_mil == '9': return 'nueve mil'
    return ''