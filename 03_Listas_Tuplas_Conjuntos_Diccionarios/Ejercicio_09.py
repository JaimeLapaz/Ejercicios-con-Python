'''
Enunciado:

9. **Filtrar por Valor**: Escribe una función que filtre un diccionario de estudiantes para obtener solo aquellos que hayan aprobado.

Solución:
'''

def filtrar_aprobados(estudiantes: dict[str, float], nota_aprobado: float = 5.0) -> dict[str, float]:
    '''
    Filtra un diccionario de estudiantes y sus calificaciones para obtener solo aquellos que han aprobado.
    
    Args:
        calificaciones (Dict[str, float]): Diccionario con nombres de estudiantes como claves y sus calificaciones como valores.
        nota_aprobatoria (float): Nota mínima para aprobar. Por defecto es 5.0.
    
    Returns:
        Dict[str, float]: Diccionario filtrado con los estudiantes que han aprobado.
    '''
    
    aprobados = {nombre: nota for nombre, nota in estudiantes.items() if nota >= nota_aprobado}
    
    return aprobados

if __name__ == "__main__":
    # Ejemplo de uso
    calificaciones_estudiantes = {
        "Juan": 5.5,
        "María": 2.0,
        "Pedro": 8.0,
        "Laura": 8.5,
        "Sofía": 4.0
    }

    estudiantes_aprobados = filtrar_aprobados(calificaciones_estudiantes)
    print("Estudiantes aprobados:")
    for nombre, nota in estudiantes_aprobados.items():
        print(f"{nombre}: {nota:.2f}")
        