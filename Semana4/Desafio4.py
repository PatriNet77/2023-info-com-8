from datetime import date
año = date.today().year

# Menú de opciones
def menu_opciones():
    while True:
        print("MUEBLERÍA ESTEBAN QUITO", "\n----- MENÚ DE OPCIONES -----")
        print("1. Agregar un inmueble")
        print("2. Editar un inmueble")
        print("3. Eliminar un inmueble")
        print("4. Cambiar el estado de un inmueble")
        print("5. Buscar inmuebles según presupuesto")
        print("6. Salir")
        
        opcion = input("\nIntroduce el número de opción: ")
        
        if opcion.isdigit() and 1 <= int(opcion) <= 6:
            return int(opcion)
        else:
            print("\nOpción inválida. Inténtalo nuevamente.")

# Agregar inmueble
def alta_inmueble(lista):
    inmueble = {}
    inmueble['año'] = int(input("Año: "))
    inmueble['metros'] = int(input("Metros cuadrados: "))
    inmueble['habitaciones'] = int(input("Cantidad de habitaciones: "))
    inmueble['garaje'] = input("¿Tiene garaje? (S/N): ").upper() == "S"
    inmueble['zona'] = input("Zona (A, B, C): ").upper()
    inmueble['estado'] = input("Estado (Disponible, Reservado, Vendido): ").capitalize()
    
    if validar_inmueble(inmueble):
        lista.append(inmueble)
        print("\nInmueble agregado exitosamente.")
    else:
        print("\nEl inmueble no cumple con las reglas de validación.")

# Validar inmueble
def validar_inmueble(inmueble):
    if (
        inmueble["zona"] in ["A", "B", "C"]
        and inmueble["estado"] in ["Disponible", "Reservado", "Vendido"]
        and inmueble["año"] >= 2000
        and inmueble["metros"] >= 60
        and inmueble["habitaciones"] >= 2
    ):
        return True
    return False

# Editar inmueble 
def editar_inmueble(lista):
    indice = int(input("Introduce el índice del inmueble a editar: "))
    
    if 0 <= indice < len(lista):
        nuevo_inmueble = {}
        nuevo_inmueble['año'] = int(input("Nuevo año: "))
        nuevo_inmueble['metros'] = int(input("Nuevos metros cuadrados: "))
        nuevo_inmueble['habitaciones'] = int(input("Nueva cantidad de habitaciones: "))
        nuevo_inmueble['garaje'] = input("¿Tiene garaje? (S/N): ").upper() == "S"
        nuevo_inmueble['zona'] = input("Nueva zona (A, B, C): ").upper()
        nuevo_inmueble['estado'] = input("Nuevo estado (Disponible, Reservado, Vendido): ").capitalize()
        
        if validar_inmueble(nuevo_inmueble):
            editar_inmueble(lista, indice, nuevo_inmueble)
        else:
            print("\nEl inmueble no cumple con las reglas de validación.")
    else:
        print("\nÍndice inválido.")

# Eliminar inmueble
def borrar_inmueble(lista):
    indice = int(input("Introduce el índice del inmueble a eliminar: "))
    
    if 0 <= indice < len(lista):
        borrar_inmueble(lista, indice)
        print("\nInmueble eliminado exitosamente.")
    else:
        print("\nÍndice inválido.")

# Cambiar estado 
def cambiar_estado(lista):
    indice = int(input("Introduce el índice del inmueble a modificar el estado: "))
    nuevo_estado = input("Introduce el nuevo estado (Disponible, Reservado, Vendido): ").capitalize()
    
    if 0 <= indice < len(lista):
        cambiar_estado(lista, indice, nuevo_estado)
        print("\nEstado del inmueble modificado exitosamente.")
    else:
        print("\nÍndice inválido.")

# Calcular el precio 
def calcular_precio(inmueble):
    zona = inmueble["zona"]
    metros = inmueble["metros"]
    habitaciones = inmueble["habitaciones"]
    garaje = inmueble["garaje"]
    antiguedad = año - inmueble["año"]

    if zona == "A":
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (año - antiguedad / 100)
    elif zona == "B":
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (año - antiguedad / 100) * 1.5
    elif zona == "C":
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (año - antiguedad / 100) * 2

    return precio

# Buscar inmuebles según presupuesto
def buscar_presupuesto(lista):
    presupuesto = float(input("Introduce el presupuesto máximo: "))
    inmuebles_encontrados = []

    for inmueble in lista:
        precio = calcular_precio(inmueble)
        if inmueble["estado"] in ["Disponible", "Reservado"] and precio <= presupuesto:
            inmueble_actualizado = inmueble.copy()
            inmueble_actualizado["precio"] = precio
            inmuebles_encontrados.append(inmueble_actualizado)

    return inmuebles_encontrados

# Lista de inmuebles
inmuebles = [{"año": 2010, "metros": 150, "habitaciones": 4, "garaje": True, "zona": "C", "estado": "Disponible"},
{"año": 2016, "metros": 80, "habitaciones": 2, "garaje": False, "zona": "B", "estado": "Reservado"},
{"año": 2000, "metros": 180, "habitaciones": 4, "garaje": True, "zona": "A", "estado": "Disponible"},
{"año": 2015, "metros": 95, "habitaciones": 3, "garaje": True, "zona": "B", "estado": "Vendido"},
{"año": 2008, "metros": 60, "habitaciones": 2, "garaje": False, "zona": "C", "estado": "Disponible"}]

# Programa principal
while True:
    opcion = menu_opciones()

    if opcion == 1:
        alta_inmueble(inmuebles)
    elif opcion == 2:
        editar_inmueble(inmuebles)
    elif opcion == 3:
        borrar_inmueble(inmuebles)
    elif opcion == 4:
        cambiar_estado(inmuebles)
    elif opcion == 5:
        inmuebles_encontrados = buscar_presupuesto(inmuebles)
        print("----- INMUEBLES ENCONTRADOS -----")
        for inmueble in inmuebles_encontrados:
            print(inmueble)
    elif opcion == 6:
        print("¡Hasta luego!")
        break

