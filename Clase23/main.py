def ordenamiento_burbuja_for (arreglo):
    # arreglo desordenado
    print(arreglo)
    largo = len(arreglo)
    # Ciclo para recorrer el arreglo
    for i in range(largo):
        # Segundo ciclo para recorrer arreglo y comparar los valores
        for j in range(1, largo):
            # Implementar evaluacion
            if arreglo[j - 1] > arreglo[j]:
                # Implementar sistema de intercambio
                aux = arreglo[j]
                arreglo[j] = arreglo[j - 1]
                arreglo[j - 1] = aux
    # arreglo ordenado
    print(arreglo)

def ordenamiento_burbuja_mejorado (arreglo):
    # arreglo ordenado
    print(arreglo)
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
    print(arreglo)
    
arreglo = [3, 4, 2, 5, 1]
arreglo2 = [3, 4, 2, 5, 1]
ordenamiento_burbuja_for(arreglo)
ordenamiento_burbuja_mejorado(arreglo2)