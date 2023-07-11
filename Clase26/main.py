# Realizar un programa que permita al usuario poder seleccionar opciones de un menu
# que le permitan realizar las 4 operaciones basicas de una base de datos, Buscar, Ingresar, Actualizar
# y Eliminar. El menu se debe mostrar hasta que el usario lo desee.
# Todas las operaciones se deben realizar en funciones separadadas, mediante el uso de lista y
# diccionarios.

# lista con diccionario con las claves: RUT, nombre, email
lista_personas = list()

# funcion para obtener indice de un registro
def buscar_registro_indice(RUT: str) -> int:
    indice = 0
    global lista_personas
    for persona in lista_personas:
        if persona["RUT"] == RUT:
            return indice
        indice = indice + 1
    return -1 

# funcion para buscar registro
def buscar_regristo():
    rut = input("Ingrese el rut a buscar: ")
    indice = buscar_registro_indice(rut)

    if indice > -1:
        print("El registro buscado corresponde a:")
        print(f"RUT: {rut}")
        global lista_personas
        registro = lista_personas[indice]
        print(f"Nombre: {registro['nombre']}")
        print(f"Email: {registro['email']}")
    else:
        print(f"El usuario con el rut {rut} no existe.")

# funcion para eliminar registro
def elminar_registro():
    pass

# funcion para actualizar registro
def actualizar_registro():
    pass

# funcion para agregar un registro (validar que registro no se encuentre duplicado)
def agregar_registro():
    rut = input("Ingrese el RUT: ")
    nombre = input("Ingrese el nombre: ")
    email = input("Ingrese el email: ")

    if buscar_registro_indice(rut) == -1:
        global lista_personas
        lista_personas.append({
            "RUT": rut,
            "nombre": nombre,
            "email": email
        })

        print("El registro fue guardado con exito!!!")
    else:
        print(f"El registro con el rut {rut} ya existe.")

# programa princiapal con el menu con las opciones
opcion = 1
while opcion >= 1 and opcion <= 4:
    print("MENU DE OPCIONES")
    print("1.- Buscar un registro")
    print("2.- Agregar un registro")
    print("3.- Modificar un registro")
    print("4.- Eliminar un registro")
    opcion = int(input("Ingrese una opcion entre 1 a 4: "))
    if opcion == 1:
        buscar_regristo()
    elif opcion == 2:
        agregar_registro()
    elif opcion == 3:
        actualizar_registro()
    elif opcion == 4:
        elminar_registro()
