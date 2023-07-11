# Listas: son dinamicas y permiten manejar cualquier tipo de dato, 
# no es necesario definirlas ya que ya se encuentran definidas
# por defecto en python
lista = [1, 2, 3] # defincion de una lista
lista2 = list([1, 2, 3]) # defincion de una lista
print(lista)
print(lista2)

# Arreglos: suelen ser estaticos (tienen un numero de elementos ya definidos),
# y tambien pueden especificar su tipo de dato. Otra particularidad es que
# soportan las operaciones matematicas.
from array import array

arreglo = array("i", [5]) # definicion de un array, donde el primer valor ("i")
# especifica el tipo de dato y el segundo, la lista de elementos.
arreglo.append(1)
# arreglo.append("A") -> esto arroja error, ya que no es del tipo de dato 
# del arreglo

# Tuplas: tambien son listas de elementos, pero no pueden ser modificadas.
# Al igual que las listas, soportan varios tipos de datos
tupla = ("A", 1, 2, 3)
print(tupla)

# Diccionarios: son listas que se basan en el concepto clave:valor,
# de este modo podemos asociar valores a nombres.
diccionario = { "RUT": "12312312-3", "nombre": "Pablo Carpio" }
print(diccionario)
print(diccionario["RUT"])
diccionario["nombre"] = "Maria Rojas"
print(diccionario)