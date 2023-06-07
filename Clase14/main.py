# Validar parentesis: Escribir un programa en python que mediante el uso de
# funciones verfique si una cadena que contiene parentesis es correctamente
# balanceado. Esto significa que cada parentesis de apertura tiene un parentesis
# de cierre correspondiente en orden correcto.
# 
# Ejemplos de inputs para validar
# (5 + 6) -> correctamente balanceado
# 5 + 6) -> incorrectamente balanceado
# (5 + 6 -> incorrectamente balanceado
# (5 * ((1 + 4) / 2)) -> correctamente balanceado
from solucion1 import *
from solucion2 import *
from solucion3 import *

print(ValidarBalanceV1('5 + 6)'))
print(ValidarBalanceV1('(5 * ((1 + 4) / 2))'))
print(ValidarBalanceV1(''))

print(ValidarBalanceV2('5 + 6)'))
print(ValidarBalanceV2('(5 * ((1 + 4) / 2))'))
print(ValidarBalanceV2(''))

print(ValidarBalanceV3('5 + 6)'))
print(ValidarBalanceV3('(5 * ((1 + 4) / 2))'))
print(ValidarBalanceV3(')('))
print(ValidarBalanceV3('((5) * ((1 + 4) / 2))'))
print(ValidarBalanceV3('((5) * (()1( + 4) / 2))'))
print(ValidarBalanceV3('())'))

print(ValidarBalanceV11('5 + 6)'))
print(ValidarBalanceV11('(5 * ((1 + 4) / 2))'))
print(ValidarBalanceV11(')('))
print(ValidarBalanceV11('((5) * ((1 + 4) / 2))'))
print(ValidarBalanceV11('((5) * (()1( + 4) / 2))'))
print(ValidarBalanceV11('())'))