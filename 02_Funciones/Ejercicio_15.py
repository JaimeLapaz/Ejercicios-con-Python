'''
Enunciado:

15. Definir una función `max_de_tres()`, que tome tres números como argumentos y 
devuelva el mayor de ellos.

Solución:
'''

def max_de_tres(num1, num2, num3):
    '''
    Calcula el máximo de tres numeros.
    
    Args:
    num1 (int o float): Primer numero.
    num2 (int o float): Segundo numero.
    num3 (int o float): Tercer numero.
    
    Return:
    int o float: El mayor de los tres numeros.
    '''
    
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

def main():
    while True:
        print("\nMenú de Opciones:")
        print("1. Números enteros.")
        print("2. Números con decimales.")
        print("3. Salir del programa.")
        opcion = input("Elige entre 1/2/3: ")
        
        if opcion == "1":
            num1 = int(input("Ingresa el primer número: "))
            num2 = int(input("Ingresa el segundo número: "))
            num3 = int(input("Ingresa el tercer número: "))
            print(f"El mayor de los tres números es: {max_de_tres(num1, num2, num3)}")
        elif opcion == "2":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            num3 = float(input("Ingresa el tercer número: "))
            print(f"El mayor de los tres números es: {max_de_tres(num1, num2, num3)}")
        elif opcion == "3":
            print("Gracias por usar el programa.")
            break
        else:
            print("Opción incorrecta. Intente de nuevo.")

if __name__ == "__main__":
    main()