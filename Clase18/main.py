def invertir_texto(texto: str) -> str:
    texto_invertido = ''
    for i in range(len(texto) - 1, -1, -1):
        texto_invertido = texto_invertido + texto[i]
    return texto_invertido

def remover_espacios(texto: str) -> str:
    texto_sin_espacios = ''
    for letra in texto:
        if letra != ' ':
            texto_sin_espacios = texto_sin_espacios + letra
    return texto_sin_espacios

def es_palindromo(texto: str) -> bool:
    patron1 = remover_espacios(texto.lower())
    patron2 = invertir_texto(patron1)
    return patron1 == patron2

def es_palindromo2(texto: str) -> bool:
    patron = remover_espacios(texto.lower())
    largo = len(patron) - 1
    es_valido = True
    indice = 0
    while es_valido and indice <= largo:
        if patron[indice] != patron[largo - indice]:
            es_valido = False
        indice = indice + 1
    return es_valido

print(es_palindromo('Anita lava la tina'))
print(es_palindromo2('Anita lava la tina'))
