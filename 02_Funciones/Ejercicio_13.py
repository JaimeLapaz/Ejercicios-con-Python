'''
Enunciado:

13. Queremos crear un programa que trabaje con fracciones a/b. 
Para representar una fracción vamos a utilizar dos enteros: numerador y denominador.

Solución:
'''
from math import gcd

def leer_fraccion():
    '''
    Lee por teclado una fracción (numerador y denominador)
    
    Return:
    tuple: Una tupla (numerador, denominador)
    '''
    
    numerador = int(input("Introduce el numerador: "))
    denominador = int(input("Introduce el denominador: "))
    if denominador == 0:
        print("El denominador no puede ser 0. Intentalo de nuevo.")
        denominador = int(input("Introduce el denominador: "))
    return numerador, denominador

def simplificar_fraccion(numerador, denominador):
    '''
    Simplifica una fracción.
    
    Args:
    numerador (int): Numerador de la fracción.
    denominador (int): Denominador de la fracción.
    
    Return:
    tuple: Una tupla (numerador_simplificado, denominador_simplificado) con la fracción simplificada
    '''
    
    frac_gcd = gcd(numerador, denominador)
    numerador_simplificado = numerador // frac_gcd
    denominador_simplificado = denominador // frac_gcd
    
    return numerador_simplificado, denominador_simplificado

def sumar_fracciones(frac1, frac2):
    '''
    Suma dos fracciones.
    
    Args:
    frac1 (tuple): Una tupla (numerador, denominador).
    frac2 (tuple): Una tupla (numerador, denominador).
    
    Return:
    tuple: Una tupla (numerador, denominador) con la suma de las dos fracciones.
    '''
    
    num1, den1 = frac1
    num2, den2 = frac2
    num_suma = num1 * den2 + num2 * den1
    den_suma = den1 * den2
    
    return simplificar_fraccion(num_suma, den_suma)

def restar_fracciones(frac1, frac2):
    '''
    Resta dos fracciones.
    
    Arggs:
    frac1 (tuple): Una tupla (numerador, denominador).
    frac2 (tuple): Una tupla (numerador, denominador).
    
    Return:
    tuple: Una tupla (numerador, denominador) con la resta de las dos fracciones.
    ''' 
    
    num1, den1 = frac1
    num2, den2 = frac2
    num_resta = num1 * den2 - num2 * den1
    den_resta = den1 * den2
    
    return simplificar_fraccion(num_resta, den_resta)

def multiplicar_fracciones(frac1, frac2):
    '''
    Multiplica dos fracciones.
    
    Args:
    frac1 (tuple): Una tupla (numerador, denominador).
    frac2 (tuple): Una tupla (numerador, denominador).
    
    Return:
    tuple: Una tupla (numerador, denominador) con la multiplicación de las dos.
    '''
    
    num1, den1 = frac1
    num2, den2 = frac2
    num_mult = num1 * num2
    den_mult = den1 * den2
    
    return simplificar_fraccion(num_mult, den_mult)

def dividir_fracciones(frac1, frac2):
    '''
    Divide dos fracciones.
    
    Args:
    frac1 (tuple): Una tupla (numerador, denominador).
    frac2 (tuple): Una tupla (numerador, denominador).
    
    Return:
    tuple: Una tupla (numerador, denominador) con la división de las dos.
    '''
    
    num1, den1 = frac1
    num2, den2 = frac2
    if num2 == 0:
        raise ValueError("No se puede dividir por una fracción con numerador cero.")
    num_div = num1 * den2
    den_div = den1 * num2
    
    return simplificar_fraccion(num_div, den_div)

def imprimir_fraccion(frac):
    """
    Imprime una fracción.
    
    Args:
    frac (tuple): La fracción (numerador, denominador).
    """
    numerador, denominador = frac
    print(f"{numerador}/{denominador}")
    
def main():
    while True:
        print("\nMenú de operaciones con fracciones:")
        print("0. Simplificar una fracción")
        print("1. Sumar fracciones")
        print("2. Restar fracciones")
        print("3. Multiplicar fracciones")
        print("4. Dividir fracciones")
        print("5. Salir")
        opcion = input("Elige una opción (0/1/2/3/4/5): ")

        if opcion == '0':
            print("Introduce la fracción:")
            numerador, denominador = leer_fraccion()
            resultado = simplificar_fraccion(numerador, denominador)
            print("La fracción simplificada es: ", end="")
            imprimir_fraccion(resultado)
            
        elif opcion in ['1', '2', '3', '4']:
            print("Introduce la primera fracción:")
            fraccion1 = leer_fraccion()
            print("Introduce la segunda fracción:")
            fraccion2 = leer_fraccion()

            if opcion == '1':
                resultado = sumar_fracciones(fraccion1, fraccion2)
                print("Resultado de la suma: ", end="")
                imprimir_fraccion(resultado)
            elif opcion == '2':
                resultado = restar_fracciones(fraccion1, fraccion2)
                print("Resultado de la resta: ", end="")
                imprimir_fraccion(resultado)
            elif opcion == '3':
                resultado = multiplicar_fracciones(fraccion1, fraccion2)
                print("Resultado de la multiplicación: ", end="")
                imprimir_fraccion(resultado)
            elif opcion == '4':
                try:
                    resultado = dividir_fracciones(fraccion1, fraccion2)
                    print("Resultado de la división: ", end="")
                    imprimir_fraccion(resultado)
                except ValueError as e:
                    print(e)
        
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, por favor elige una opción válida.")

if __name__ == "__main__":
    main()