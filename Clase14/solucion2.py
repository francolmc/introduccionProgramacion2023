from utils import *

def ValidarBalanceV2(texto: str) -> bool:
    if texto == '':
        return False
    
    contador_apertura = 0
    contador_cierre = 0
    for caracter in texto:
        if esLlaveDeApertura(caracter):
            contador_apertura = contador_apertura + 1
        elif esLlaveDeCierre(caracter):
            contador_cierre = contador_cierre + 1

    if contador_apertura == contador_cierre:
        return True
    return False