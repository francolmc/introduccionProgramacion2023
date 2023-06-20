def es_vocal(letra: str) -> bool:
    es_vocal_variable = False
    if letra.upper() == 'A': es_vocal_variable = True
    if letra.upper() == 'E': es_vocal_variable = True
    if letra.upper() == 'I': es_vocal_variable = True
    if letra.upper() == 'O': es_vocal_variable = True
    if letra.upper() == 'U': es_vocal_variable = True
    return es_vocal_variable

def vocales_mayusculas(texto: str) -> str:
    nuevo_texto = ''
    for letra in texto:
        if es_vocal(letra):
            nuevo_texto = nuevo_texto + letra.upper()
        else:
            nuevo_texto = nuevo_texto + letra
    print(nuevo_texto)


opcion = 's'
while opcion == 's':
    texto = input('Ingrese un texto: ')
    print('Resultado: ')
    vocales_mayusculas(texto)
    opcion = input('Desea ingresar otro texto? [s/n]: ')