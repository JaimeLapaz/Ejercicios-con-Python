''''
Enunciado:

3. Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel 
primario de una escuela, finalizando al ingresar “x”. A continuación,
solicitar que ingrese los nombres de los alumnos de nivel secundario, 
finalizando al ingresar “x”.

- Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario,
sin repeticiones.
- Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
- Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

Solución:
'''
from typing import Set

def ingresar_nombres(alumnos_tipo: str) -> Set[str]:
    '''
    Solicita al usuario ingresar nombres de alumnos y devuelve un conjunto con esos nombres.
    
    Args:
    alumnos_tipo (str): tipo de alumnos (primario o secundario)
    
    Return:
    set: conjunto de nombres de alumnos
    '''
    
    nombres = set()
    while True:
        nombre = input(f"Ingrese el nombre de un alumno de {alumnos_tipo} o escribe 'x' para salir: ").strip()
        if nombre.lower() == 'x':
            break
        if nombre:
            nombres.add(nombre)
        
    return nombres

def main():
    # Ingresando los nombres de los alumnos de nivel primario
    print("Ingreso de nombres de los alumnos de nivel primario: ")
    alumnos_primario = ingresar_nombres("nivel primario")
    
    # Ingresando los nombres de los alumnos de nivel secundario
    print("Ingreso de nombres de los alumnos de nivel primario: ")
    alumnos_secundario = ingresar_nombres("nivel secundario")
    
    # Nombres que se repiten entre primario y secundario
    nombres_repetidos = alumnos_primario.intersection(alumnos_secundario)
    print("\nNombres que se repiten entre nivel primario y secundario:")
    print(", ".join(nombres_repetidos) if nombres_repetidos else "No hay nombres repetidos.")

    # Nombres de nivel primario que no se repiten en secundario
    nombres_unicos_primario = alumnos_primario.difference(alumnos_secundario)
    print("\nNombres de nivel primario que no se repiten en secundario:")
    print(", ".join(nombres_unicos_primario) if nombres_unicos_primario else "No hay nombres únicos en nivel primario.")
    
if __name__ == "__main__":
    main()