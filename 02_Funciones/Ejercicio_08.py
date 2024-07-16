'''
Enunciado:

8. Crear una función recursiva que permita calcular el factorial de un número. 
Realiza un programa principal donde se lea un entero y se muestre el resultado del factorial.

Solución:
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    n = int(input("Ingrese un número: "))
    print(f"El factorial de {n} es {factorial(n)}")
    
if __name__ == "__main__":
    main()