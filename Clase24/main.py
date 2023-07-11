def ordenamiento_burbuja_mejorado (arreglo):
    largo = len(arreglo)
    # Ciclo para recorrer el arreglo
    for i in range(largo):
        hay_cambio = False
        for j in range(1, largo - i):
            if arreglo[j - 1] > arreglo[j]:
                aux = arreglo[j - 1]
                arreglo[j - 1] = arreglo[j]
                arreglo[j] = aux
                hay_cambio = True
        if not hay_cambio:
            break
    return arreglo

def busqueda_binaria(arreglo, elemento):
    izquierda = 0
    derecha = len(arreglo) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if arreglo[medio] == elemento:
            return medio
        elif elemento > arreglo[medio]:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

def busqueda_binaria_recursiva(arreglo, elemento, izquierda, derecha):
    if izquierda > derecha:
        return -1
    medio = (izquierda + derecha) // 2
    if elemento == arreglo[medio]:
        return medio
    elif elemento > arreglo[medio]:
        return busqueda_binaria_recursiva(arreglo, elemento, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(arreglo, elemento, izquierda, medio - 1)


lista = [4,6,1,2,3,8,5]
print(lista)
lista = ordenamiento_burbuja_mejorado(lista)
print(lista)

resultado = busqueda_binaria(lista, 5)
print(resultado)

resultado2 = busqueda_binaria_recursiva(lista, 5, 0, len(lista) - 1)
print(resultado2)