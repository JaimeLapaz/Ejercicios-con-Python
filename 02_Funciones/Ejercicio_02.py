'''
Enunciado:

2. Crear un programa que pida dos números enteros al usuario y 
diga si alguno de ellos es múltiplo del otro. 
Crear una función `EsMultiplo` que reciba los dos números y 
devuelva si el primero es múltiplo del segundo.

Solución:
'''

def EsMultiplo(a, b):
    """Determina si a es múltiplo de b."""
    if b == 0:
        return False  # No se puede dividir por cero
    return a % b == 0

def main():
    # Pedir dos números enteros al usuario
    numero1 = int(input("Introduce el primer número entero: "))
    numero2 = int(input("Introduce el segundo número entero: "))

    # Verificar si alguno es múltiplo del otro
    if EsMultiplo(numero1, numero2):
        print(f"{numero1} es múltiplo de {numero2}.")
    elif EsMultiplo(numero2, numero1):
        print(f"{numero2} es múltiplo de {numero1}.")
    else:
        print("Ninguno de los números es múltiplo del otro.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()