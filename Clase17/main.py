def es_par(valor: int) -> bool:
    if valor%2 == 0:
        return True
    return False

def es_impar(valor: int) -> bool:
    if valor%2 != 0:
        return True
    return False

def separar_numeros(valor: str) -> str:
    numeros = valor.split(',')
    pares = ''
    impares = ''
    for numero in numeros:
        if numero.isnumeric():
            if es_par(int(numero)):
                pares = pares + numero + ','
            if es_impar(int(numero)):
                impares = impares + numero + ','
    return pares + impares 
        

resultado = separar_numeros('A,1,2,3,4,5,6,7,8,9')

print(resultado)
