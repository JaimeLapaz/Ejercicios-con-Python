"""Ejercicio 280 — Matriz de Rotación 3D.

Enunciado:
    Desarrolla una función que genere una matriz de rotación 3D para
    una transformación espacial.

Solución:
    Utilizar la fórmula de Rodrigues para obtener una matriz 3 x 3
    que gira un ángulo en radianes alrededor de un eje arbitrario.
    Se normaliza el eje y se aplica la convención de la mano derecha.
    La rotación es activa sobre vectores columna.
"""
from collections.abc import Sequence
from math import cos, isclose, isfinite, pi, sin, sqrt

Vector3 = Sequence[int | float]
Matriz3 = list[list[float]]


def matriz_rotacion_3d(eje: Vector3, angulo: float) -> Matriz3:
    """Devolver la rotación de Rodrigues para un eje no nulo.

    El ángulo se expresa en radianes; un valor positivo sigue
    la regla de la mano derecha.
    """
    if len(eje) != 3:
        raise ValueError("El eje debe tener tres componentes")
    if (
        isinstance(angulo, bool)
        or not isinstance(angulo, (int, float))
        or not isfinite(angulo)
    ):
        raise ValueError("El ángulo debe ser un número finito")
    if any(
        isinstance(x, bool) or not isinstance(x, (int, float)) or not isfinite(x)
        for x in eje
    ):
        raise ValueError("El eje debe contener tres números finitos")
    # hypot evita desbordamientos intermedios al normalizar.
    from math import hypot

    norma = hypot(*eje)
    if norma == 0:
        raise ValueError("El eje de rotación no puede ser nulo")
    x, y, z = (componente / norma for componente in eje)
    c, s = cos(angulo), sin(angulo)
    t = 1.0 - c
    return [
        [t*x*x + c,   t*x*y - s*z, t*x*z + s*y],
        [t*x*y + s*z, t*y*y + c,   t*y*z - s*x],
        [t*x*z - s*y, t*y*z + s*x, t*z*z + c],
    ]


def rotar_vector(matriz: Matriz3, vector: Vector3) -> list[float]:
    """Aplicar una matriz de rotación 3 x 3 a un vector columna."""
    if len(vector) != 3 or len(matriz) != 3 or any(len(f) != 3 for f in matriz):
        raise ValueError("Se requieren una matriz 3 x 3 y un vector 3D")
    return [sum(matriz[i][j] * vector[j] for j in range(3)) for i in range(3)]


if __name__ == '__main__':
    identidad = matriz_rotacion_3d((1, 2, 3), 0)
    for i in range(3):
        for j in range(3):
            assert isclose(identidad[i][j], float(i == j), abs_tol=1e-12)

    giro = matriz_rotacion_3d((0, 0, 5), pi / 2)
    resultado = rotar_vector(giro, (1, 0, 0))
    assert all(isclose(a, b, abs_tol=1e-12) for a, b in zip(resultado, (0, 1, 0)))
    assert all(isclose(a, b, abs_tol=1e-12) for a, b in
               zip(rotar_vector(giro, (0, 0, 2)), (0, 0, 2)))

    # Las columnas de cualquier rotación forman una base ortonormal.
    for eje, angulo in (((1, 2, 3), 0.7), ((1, 0, 0), pi), ((0, 1, 0), -0.4)):
        r = matriz_rotacion_3d(eje, angulo)
        for i in range(3):
            for j in range(3):
                producto = sum(r[k][i] * r[k][j] for k in range(3))
                assert isclose(producto, float(i == j), abs_tol=1e-12)
        det = (
            r[0][0] * (r[1][1]*r[2][2] - r[1][2]*r[2][1])
            - r[0][1] * (r[1][0]*r[2][2] - r[1][2]*r[2][0])
            + r[0][2] * (r[1][0]*r[2][1] - r[1][1]*r[2][0])
        )
        assert isclose(det, 1.0, abs_tol=1e-12)

    for eje, angulo in (((0, 0, 0), 1), ((1, 2), 1),
                        ((float('inf'), 0, 0), 1), ((1, 0, 0), float('nan'))):
        try:
            matriz_rotacion_3d(eje, angulo)
        except ValueError:
            pass
        else:
            raise AssertionError("Se aceptó una rotación inválida")
    print("Ejercicio 280: pruebas superadas")
