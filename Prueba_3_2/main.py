def es_consonante(letra: str) -> bool:
    es_consonante_variable = False
    if letra.upper() != 'A': 
        if letra.upper() != 'E': 
            if letra.upper() != 'I': 
                if letra.upper() != 'O':
                    if letra.upper() != 'U': 
                        es_consonante_variable = True
    return es_consonante_variable

def consonantes_mayusculas(texto: str) -> str:
    nuevo_texto = ''
    for letra in texto:
        if es_consonante(letra):
            nuevo_texto = nuevo_texto + letra.upper()
        else:
            nuevo_texto = nuevo_texto + letra
    print(nuevo_texto)


opcion = 's'
while opcion == 's':
    texto = input('Ingrese un texto: ')
    print('Resultado: ')
    consonantes_mayusculas(texto)
    opcion = input('Desea ingresar otro texto? [s/n]: ')