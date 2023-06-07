from utils import *

def ValidarBalanceV1(texto: str) -> bool:
    if texto == '':
        return False
    
    contador = 0
    for caracter in texto:
        if esLlaveDeApertura(caracter):
            contador = contador + 1
        elif esLlaveDeCierre(caracter):
            contador = contador - 1

    if contador == 0:
        return True
    return False
    # return contador == 0

def ValidarBalanceV11(texto: str) -> bool:
    if len(texto) < 2:
        return False
    
    contador = 0
    for caracter in texto:
        if esLlaveDeApertura(caracter):
            contador = contador + 1
        elif esLlaveDeCierre(caracter):
            contador = contador - 1
        if contador < 0:
            return False

    if contador == 0:
        return True
    return False
    # return contador == 0