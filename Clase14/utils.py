def esLlaveDeApertura(caracter: str) -> bool:
    if caracter == '(':
        return True
    return False

def esLlaveDeCierre(caracter: str) -> bool:
    if caracter == ')':
        return True
    return False