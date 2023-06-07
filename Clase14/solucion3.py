# recorrer el string mitad por mitad
# (5 * ((1 + 4) / 2)) en este ejemplo se recorre por separado
# por un lado (5 * ((1 +
# por otro lado  4) / 2))
# )(
from utils import *

def ValidarBalanceV3(texto: str) -> bool:
    largo_texto = len(texto) # esta funcion len me informa la cantidad de caracteres del string
    posicion_inicial = 0
    posicion_final = largo_texto - 1
    if largo_texto < 2:
        return False
    
    contador_apertura = 0
    contador_cierre = 0
    while posicion_inicial < posicion_final:
        if esLlaveDeApertura(texto[posicion_inicial]):
            contador_apertura = contador_apertura + 1
        if esLlaveDeCierre(texto[posicion_final]):
            contador_cierre = contador_cierre + 1

        posicion_inicial = posicion_inicial + 1
        posicion_final = posicion_final - 1

    print("A:", contador_apertura, "C:", contador_cierre)