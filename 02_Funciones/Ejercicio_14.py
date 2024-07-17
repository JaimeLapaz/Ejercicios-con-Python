'''
Enunciado:

14. Definir una función `max()` que tome como argumento dos números y devuelva el mayor de ellos. 
(Es cierto que Python tiene una función `max()` incorporada, pero hacerla nosotros mismos es un 
muy buen ejercicio).

Solución:
'''

def calcular_maximo(num1, num2):
    '''
    Calcula el máximo de dos numeros.
    
    Arggs:
    num1 (int): Primer numero.
    num2 (int): Segundo numero.
    
    Return:
    int: El mayor de los dos numeros.
    '''
    if num1 > num2:
        return num1
    else:
        return num2

def main():
    '''
    Programa principal que solicita dos numeros al usuario y ejecuta la función máximo.
    '''
    
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    maximo = calcular_maximo(num1, num2)
    print(f"\nEl máximo de {num1} y {num2} es: {maximo}")
    
if __name__ == "__main__":
    main()