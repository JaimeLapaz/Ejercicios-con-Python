'''
Enunciado:

9. Crear una función que calcule el MCD de dos números por el método de Euclides. 
El método de Euclides es el siguiente:
    - Se divide el número mayor entre el menor.
    - Si la división es exacta, el divisor es el MCD.
    - Si la división no es exacta, dividimos el divisor entre el resto obtenido y 
    se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
    - Crear un programa principal que lea dos números enteros y muestre el MCD.

Solución:
'''

def EuclidesMCD(num1, num2):
    '''
    Calcula el MCD usando el algoritmo de Euclides.
    
    Args:
        num1 (int): numero 1
        num2 (int): numero 2
    
    Return:
        int: el máximo común divisor.
    '''
    
    # Comprobamos que número es mayor y menor
    if num1 > num2:
        mayor = num1
        menor = num2
    else:
        mayor = num2
        menor = num1
        
    # Calculamos el resto
    resto = mayor % menor
    
    # Comprobamos si tenemos el MCD 
    if resto == 0:
        return menor
    else:
        return EuclidesMCD(menor, resto)
    
def main():
    # Pedimos los dos numeros
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    
    print("El MCD de los dos números es: ", EuclidesMCD(num1,num2))

if __name__ == "__main__":
    main()