def factoriaConFor(n: int) -> int:
    multiplicacion = 1
    for i in range(n):
        multiplicacion = multiplicacion * (i+1) # sumamos 1 pq el primer valor es cero

    return multiplicacion

def factorialRecursivo(n: int) -> int:
    if n > 1:
        return n * factorialRecursivo(n - 1)
    elif n == 1:
        return 1
    
# Calculo del factorial recursivo refactorizado
def factorialRecursivo2(n: int) -> int:
    if n > 1:
        return n * factorialRecursivo2(n - 1)
    return 1