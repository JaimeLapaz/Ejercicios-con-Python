"""Ejercicio 283 — Matrices Sparse.

Enunciado:
    Diseña una estructura de datos para representar matrices sparse
    (con muchos elementos iguales a cero) y realiza operaciones
    eficientes en ellas.

Solución:
    Guardar únicamente los elementos no nulos en diccionarios por fila.
    La suma, trasposición y multiplicación recorren entradas almacenadas,
    sin convertir las matrices a formato denso. El almacenamiento es
    proporcional al número de elementos no nulos.
"""
from collections.abc import Sequence

Numero = int | float


class MatrizDispersa:
    """Matriz rectangular con índices desde cero y ceros implícitos."""

    def __init__(self, filas: int, columnas: int) -> None:
        if filas <= 0 or columnas <= 0:
            raise ValueError("Las dimensiones deben ser positivas")
        self.filas = filas
        self.columnas = columnas
        self._datos: dict[int, dict[int, Numero]] = {}

    def _validar_indice(self, i: int, j: int) -> None:
        if not (0 <= i < self.filas and 0 <= j < self.columnas):
            raise IndexError("Índice fuera de la matriz")

    def obtener(self, i: int, j: int) -> Numero:
        self._validar_indice(i, j)
        return self._datos.get(i, {}).get(j, 0)

    def asignar(self, i: int, j: int, valor: Numero) -> None:
        self._validar_indice(i, j)
        if valor != 0:
            self._datos.setdefault(i, {})[j] = valor
        elif i in self._datos:
            self._datos[i].pop(j, None)
            if not self._datos[i]:
                del self._datos[i]

    @property
    def no_nulos(self) -> int:
        return sum(len(fila) for fila in self._datos.values())

    @classmethod
    def desde_densa(cls, matriz: Sequence[Sequence[Numero]]) -> "MatrizDispersa":
        if not matriz or not matriz[0]:
            raise ValueError("Se requiere una matriz no vacía")
        columnas = len(matriz[0])
        if any(len(fila) != columnas for fila in matriz):
            raise ValueError("La matriz debe ser rectangular")
        resultado = cls(len(matriz), columnas)
        for i, fila in enumerate(matriz):
            for j, valor in enumerate(fila):
                if valor != 0:
                    resultado.asignar(i, j, valor)
        return resultado

    def a_densa(self) -> list[list[Numero]]:
        """Materializar todos los ceros; útil para matrices pequeñas."""
        resultado = [[0] * self.columnas for _ in range(self.filas)]
        for i, fila in self._datos.items():
            for j, valor in fila.items():
                resultado[i][j] = valor
        return resultado

    def sumar(self, otra: "MatrizDispersa") -> "MatrizDispersa":
        if (self.filas, self.columnas) != (otra.filas, otra.columnas):
            raise ValueError("Las dimensiones deben coincidir")
        resultado = MatrizDispersa(self.filas, self.columnas)
        resultado._datos = {i: fila.copy() for i, fila in self._datos.items()}
        for i, fila in otra._datos.items():
            for j, valor in fila.items():
                resultado.asignar(i, j, resultado.obtener(i, j) + valor)
        return resultado

    def trasponer(self) -> "MatrizDispersa":
        resultado = MatrizDispersa(self.columnas, self.filas)
        for i, fila in self._datos.items():
            for j, valor in fila.items():
                resultado.asignar(j, i, valor)
        return resultado

    def multiplicar(self, otra: "MatrizDispersa") -> "MatrizDispersa":
        if self.columnas != otra.filas:
            raise ValueError("Dimensiones incompatibles para el producto")
        resultado = MatrizDispersa(self.filas, otra.columnas)
        # A[i,k] solo contribuye con los elementos no nulos de B[k,:].
        for i, fila in self._datos.items():
            acumulados: dict[int, Numero] = {}
            for k, a in fila.items():
                for j, b in otra._datos.get(k, {}).items():
                    acumulados[j] = acumulados.get(j, 0) + a * b
            for j, valor in acumulados.items():
                if valor != 0:
                    resultado.asignar(i, j, valor)
        return resultado


if __name__ == '__main__':
    a = MatrizDispersa.desde_densa([[0, 2, 0], [3, 0, 4]])
    b = MatrizDispersa.desde_densa([[0, -2, 5], [0, 0, -4]])
    assert a.no_nulos == 3
    assert a.sumar(b).a_densa() == [[0, 0, 5], [3, 0, 0]]
    assert a.sumar(b).no_nulos == 2
    assert a.trasponer().a_densa() == [[0, 3], [2, 0], [0, 4]]
    c = MatrizDispersa.desde_densa([[1, 0], [0, 5], [-1, 0]])
    assert a.multiplicar(c).a_densa() == [[0, 10], [-1, 0]]
    assert a.a_densa() == [[0, 2, 0], [3, 0, 4]]
    assert a.multiplicar(MatrizDispersa(3, 2)).no_nulos == 0
    # Una matriz enorme no requiere reservar espacio para sus ceros.
    grande = MatrizDispersa(1_000_000, 1_000_000)
    grande.asignar(999_999, 0, 7)
    assert grande.trasponer().obtener(0, 999_999) == 7
    grande.asignar(999_999, 0, 0)
    assert grande.no_nulos == 0
    for operacion in (lambda: a.obtener(-1, 0),
                      lambda: a.sumar(c),
                      lambda: a.multiplicar(a),
                      lambda: MatrizDispersa.desde_densa([[1], [2, 3]])):
        try:
            operacion()
        except (ValueError, IndexError):
            pass
        else:
            raise AssertionError("Se aceptó una operación inválida")
    print("Ejercicio 283: pruebas superadas")
