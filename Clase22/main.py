# definicion de una matriz
valores = [ 
    [1, 2, 3, 4, 5], 
    [6, 7, 8, 9, 0], 
    [1, 2, 3, 4, 5], 
    [6, 7, 8, 9, 0], 
    [1, 2, 3, 4, 5] 
    ]

# como recorrer una matriz
for fila in range(5): # Este for hace referencia a la fila
    for columna in range(5): # Este for hace referencia a la columna
        print(f'[{fila},{columna}] : {valores[fila][columna]}')

# informar la suma curzada de la matriz con un solo ciclo for
suma = 0
for i in range(5):
    suma = suma + valores[i][i] + valores[i][4 - i]

print(suma)
