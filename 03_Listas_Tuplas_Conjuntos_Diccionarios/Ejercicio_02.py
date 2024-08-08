'''
Enunciado:

2. Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). 
Ejemplo:
   [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")]

Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo:

   [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")]

Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:

- Agregar pasajeros a la lista de viajeros.
- Agregar ciudades a la lista de ciudades.
- Dado el DNI de un pasajero, ver a qué ciudad viaja.
- Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
- Dado el DNI de un pasajero, ver a qué país viaja.
- Dado un país, mostrar cuántos pasajeros viajan a ese país.
- Salir del programa.

Solución:
'''
def menu():
    print("\nMenú:")
    print("1. Agregar pasajero")
    print("2. Agregar ciudad")
    print("3. Ver ciudad por DNI de pasajero")
    print("4. Ver cantidad de pasajeros por ciudad")
    print("5. Ver país por DNI de pasajero")
    print("6. Ver cantidad de pasajeros por país")
    print("7. Salir")

def agregar_pasajero(viajeros):
    '''
    Esta función agrega viajeros a la lista.
    
    Args:
    viajeros (list): lista de tuplas con la información de los viajeros.
    
    Return:
    list: lista de tuplas con la información de los viajeros actualizada.
    '''
    nombre = input("Ingrese el nombre del pasajero: ")
    dni = int(input("Ingrese el DNI del pasajero: "))
    destino = input("Ingrese el destino del pasajero: ")
    viajeros.append((nombre, dni, destino))
    print("Pasajero agregado correctamente.")
    return viajeros

def agregar_ciudad(ciudades):
    '''
    Esta función agrega ciudades y paises a la lista de ciudades.
    
    Args:
    ciudades (list): lista de tuplas con la información de las ciudades.
    
    Return:
    list: lista de tuplas con la información de las ciudades actualizada.
    '''
    ciudad = input("Ingrese el nombre de la ciudad: ")
    pais = input("Ingrese el nombre del país: ")
    ciudades.append((ciudad, pais))
    print("Ciudad agregada correctamente.")
    return ciudades

def ver_ciudad_por_dni(viajeros):
    '''
    Busca la ciudad dado un dni.
    
    Args:
    viajeros (list): lista de tuplas con la información de los viajeros.
    
    Return:
    None
    '''
    dni = int(input("Ingrese el DNI del pasajero: "))
    for pasajero in viajeros:
        if pasajero[1] == dni:
            print(f"El pasajero con DNI {dni} viaja a {pasajero[2]}.")
            return
    print("Pasajero no encontrado.")

def cantidad_pasajeros_por_ciudad(viajeros):
    '''
    Esta función te dice el número de pasajeros que hay por una ciudad ingresada.
    
    Args:
    viajeros (list): lista de tuplas con la información de los viajeros.
    
    Return:
    None
    '''
    ciudad = input("Ingrese el nombre de la ciudad: ")
    count = sum(1 for pasajero in viajeros if pasajero[2] == ciudad)
    print(f"La cantidad de pasajeros que viajan a {ciudad} es {count}.")

def ver_pais_por_dni(viajeros, ciudades):
    '''
    Esta función dice los pasajeros que viajan a una ciudad por el dni.
    
    Args:
    viajeros (list): lista de tuplas con la información de los viajeros.
    ciudades (list): lista de tuplas con la información de las ciudades.
    
    Return:
    None
    '''
    dni = int(input("Ingrese el DNI del pasajero: "))
    for pasajero in viajeros:
        if pasajero[1] == dni:
            destino = pasajero[2]
            for ciudad in ciudades:
                if ciudad[0] == destino:
                    print(f"El pasajero con DNI {dni} viaja a {ciudad[1]}.")
                    return
    print("Pasajero o ciudad no encontrados.")

def cantidad_pasajeros_por_pais(viajeros, ciudades):
    '''
    Esta función imprime la cantidad de pasajeros que viaja a cada pais.
    
    Args:
    viajeros (list): lista de tuplas con la información de los viajeros.
    ciudades (list): lista de tuplas con la información de las ciudades.
    
    Return:
    None
    '''
    pais = input("Ingrese el nombre del país: ")
    ciudades_del_pais = [ciudad[0] for ciudad in ciudades if ciudad[1] == pais]
    count = sum(1 for pasajero in viajeros if pasajero[2] in ciudades_del_pais)
    print(f"La cantidad de pasajeros que viajan a {pais} es {count}.")

def main():
    viajeros = [("Manuel Juarez", 19823451, "Liverpool"), 
                ("Silvana Paredes", 22709128, "Buenos Aires"), 
                ("Rosa Ortiz", 15123978, "Glasgow"), 
                ("Luciana Hernandez", 38981374, "Lisboa")]
    ciudades = [("Buenos Aires","Argentina"), 
                ("Glasgow","Escocia"), 
                ("Lisboa", "Portugal"), 
                ("Liverpool","Inglaterra"), 
                ("Madrid","España")]

    while True:
        menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            viajeros = agregar_pasajero(viajeros)
        elif opcion == 2:
            ciudades = agregar_ciudad(ciudades)
        elif opcion == 3:
            ver_ciudad_por_dni(viajeros)
        elif opcion == 4:
            cantidad_pasajeros_por_ciudad(viajeros)
        elif opcion == 5:
            ver_pais_por_dni(viajeros, ciudades)
        elif opcion == 6:
            cantidad_pasajeros_por_pais(viajeros, ciudades)
        elif opcion == 7:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()
