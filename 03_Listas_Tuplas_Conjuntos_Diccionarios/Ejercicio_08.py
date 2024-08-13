'''
Enunciado:

8. **Calcular Promedio**: Dado un diccionario de estudiantes y sus calificaciones, calcula el promedio de calificaciones.

Solución:
'''

def calcular_promedio(estudiantes: dict[str, float]) -> float:
    """
    Calcula el valor promedio de las calificaciones de los estudiantes.
    
    Args:
    estudiantes (dict[str, float]): Diccionario con estudiantes como claves y sus calificaciones como valores.
    
    Return:
    float: El valor promedio de las calificaciones.
    """
    notas = sum(estudiantes.values())
    cantidad_estudiantes = len(estudiantes)
    
    if cantidad_estudiantes == 0:
        return 0.0
    
    promedio = round(notas / cantidad_estudiantes, 2)
    
    return promedio

if __name__ == "__main__":
    # Ejemplo de uso
    calificaciones_estudiantes = {
        "Juan": 85.5,
        "María": 92.0,
        "Pedro": 78.0,
        "Laura": 88.5,
        "Sofía": 91.0
    }

    promedio = calcular_promedio(calificaciones_estudiantes)
    print(f"La calificación promedia es: {promedio}")