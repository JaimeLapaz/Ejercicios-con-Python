'''
Enunciado:

6. Crear un programa para gestionar datos de los socios de un club, permitiendo:

- Cargar información de los socios en un diccionario para acceder por número de socio. Los datos a almacenar son: número, nombre y apellido, 
fecha de ingreso (ddmmaaaa), cuota al día (s/n). El programa debe iniciar con los datos de los socios fundadores ya cargados:
  - Socio nº1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
  - Socio nº2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
  - Socio nº3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
- Informar cantidad de socios del club.
-Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas
adeudadas.
- Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que
en realidad ingresaron el 14/03/2018.
- Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado).
- Imprimir el listado de socios completo.

Solución:
'''

from typing import Dict, Optional

# Definición inicial de los socios fundadores
SOCIOS_INICIALES = {
    1: {"nombre_completo": "Amanda Núñez", "fecha_ingreso": "17/03/2009", "cuota_al_dia": True},
    2: {"nombre_completo": "Bárbara Molina", "fecha_ingreso": "17/03/2009", "cuota_al_dia": True},
    3: {"nombre_completo": "Lautaro Campos", "fecha_ingreso": "17/03/2009", "cuota_al_dia": True}
}

socios = SOCIOS_INICIALES.copy()

def obtener_cantidad_socios() -> int:
    """
    Informa la cantidad actual de socios.
    """
    return len(socios)

def registrar_pago_cuotas(numero_socio: int) -> None:
    """
    Marca como al día las cuotas del socio especificado por número de socio.
    
    Args:
    numero_socio (int): Número de socio.
    
    Return:
    None
    """
    if numero_socio in socios:
        socios[numero_socio]["cuota_al_dia"] = True
        print(f"Socio {numero_socio} ha pagado todas las cuotas.")
    else:
        print(f"Socio con número {numero_socio} no encontrado.")

def actualizar_fecha_ingreso(fecha_anterior: str, nueva_fecha: str) -> None:
    """
    Modifica la fecha de ingreso de los socios que ingresaron en una fecha específica.
    
    Args:
    fecha_anterior (str): Fecha de ingreso anterior.
    nueva_fecha (str): Fecha de ingreso nueva.
    
    Return:
    None
    """
    for socio in socios.values():
        if socio["fecha_ingreso"] == fecha_anterior:
            socio["fecha_ingreso"] = nueva_fecha
    print(f"Fechas de ingreso actualizadas de {fecha_anterior} a {nueva_fecha}.")

def dar_de_baja_socio(nombre: str, apellido: str) -> None:
    """Elimina a un socio por su nombre y apellido."""
    nombre_completo: str = f"{nombre} {apellido}"
    socio_a_eliminar: Optional[int] = None
    
    for numero_socio, socio in socios.items():
        if socio["nombre_completo"] == nombre_completo:
            socio_a_eliminar = numero_socio
            break

    if socio_a_eliminar:
        del socios[socio_a_eliminar]
        print(f"Socio {nombre_completo} ha sido dado de baja.")
    else:
        print(f"Socio {nombre_completo} no encontrado.")

def imprimir_listado_socios() -> None:
    """Imprime el listado completo de los socios."""
    for numero_socio, socio in socios.items():
        print(f"Número de socio: {numero_socio}")
        print(f"Nombre: {socio['nombre_completo']}")
        print(f"Fecha de ingreso: {socio['fecha_ingreso']}")
        print(f"Cuota al día: {'Sí' if socio['cuota_al_dia'] else 'No'}")
        print("-" * 30)

if __name__ == "__main__":
    # Ejemplo de uso
    print(f"Cantidad de socios: {obtener_cantidad_socios()}")
    
    # Registrar el pago de cuotas de un socio
    registrar_pago_cuotas(2)
    
    # Modificar fecha de ingreso para socios ingresados el 13/03/2018
    actualizar_fecha_ingreso("13/03/2018", "14/03/2018")
    
    # Dar de baja a un socio
    dar_de_baja_socio("Lautaro", "Campos")
    
    # Imprimir el listado de socios completo
    imprimir_listado_socios()