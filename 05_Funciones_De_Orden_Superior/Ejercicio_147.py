"""
Enunciado:

147. Generación de Números Primos: Crea una función de orden superior
que genere números primos utilizando el algoritmo de la criba de
Eratóstenes.

Solución:
"""

from collections.abc import Callable


def generar_primos(
    limite: int,
    procesar: Callable[[list[int]], list[int]],
) -> list[int]:
    """Genera los primos hasta el límite y aplica una función al resultado."""
    if limite < 2:
        return procesar([])

    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False

    divisor = 2
    while divisor * divisor <= limite:
        if es_primo[divisor]:
            for multiplo in range(divisor * divisor, limite + 1, divisor):
                es_primo[multiplo] = False
        divisor += 1

    primos = [
        numero for numero, primo in enumerate(es_primo) if primo
    ]
    return procesar(primos)


if __name__ == "__main__":
    primos = generar_primos(30, lambda numeros: numeros)
    primos_mayores_de_diez = generar_primos(
        30, lambda numeros: [numero for numero in numeros if numero > 10]
    )

    print("Primos hasta 30:", primos)
    print("Primos mayores de 10:", primos_mayores_de_diez)
    assert primos == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert primos_mayores_de_diez == [11, 13, 17, 19, 23, 29]
    assert generar_primos(1, lambda numeros: numeros) == []
