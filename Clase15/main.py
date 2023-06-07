# Realizar un programa en Python que reciba un string largo e informe cuantas
# veces se repiten las letras en un texto. Por ejemplo:
# "Esto es un texto cualquiera"
# resultado: E(4), s(2), t(3)...

# Realizar un programa en Python que reciba un string largo e informe cuantas
# veces se repiten cada palabra. Por ejemplo:
# "cada dia es un dia diferente"
# resultado cada(1), dia(2), es(1), un(1), diferente(1)

# texto = "Cada dia es un dia diferente"
# palabras = texto.split(' ')
# for palabra in palabras:
#     print(palabra.lower())
#     print(palabra.upper())

# Solicitar una frase al usurio
frase = input('Ingrese una frase: ')
# transformar a minuscula la frase completa
frase_minusculas = frase.lower()
# un ciclo for para recorrer la frase palabra por palabra
for letra in frase_minusculas:
    # agregar un contador
    contador = 0
    # contar cuantas letras hay en la frase
    for letra2 in frase_minusculas:
        if letra == letra2:
            contador = contador + 1
    print(letra, ':', contador)
    

texto = input('Ingresa un texto: ')
minusculas = texto.lower()
palabras = texto.split(' ')
for palabra in palabras:
    contador = 0
    for palabra2 in palabras:
        if palabra == palabra2:
            contador = contador + 1
    print(palabra, ':', contador)