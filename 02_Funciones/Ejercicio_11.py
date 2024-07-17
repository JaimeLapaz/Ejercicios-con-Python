''' 
Enunciado:

11. El día juliano correspondiente a una fecha es un número entero que indica los días que 
han transcurrido desde el 1 de enero del año indicado. 
Queremos crear un programa principal que al introducir una fecha nos diga el día juliano 
que corresponde. Para ello podemos hacer las siguientes subrutinas:
    - `LeerFecha`: Nos permite leer por teclado una fecha (día, mes y año).
    - `DiasDelMes`: Recibe un mes y un año y nos dice los días de ese mes en ese año.
    - `EsBisiesto`: Recibe un año y nos dice si es bisiesto.
    - `Calcular_Dia_Juliano`: Recibe una fecha y nos devuelve el día juliano.
'''

def LeerFecha():
    '''
    Lee por teclado una fecha (día, mes, año).
    
    Return:
    tuple: Una tupla (día, mes, año).
    '''
    
    dia = int(input('Introduce el día: '))
    mes = int(input('Introduce el mes: '))
    año = int(input('Introduce el año: '))
    
    return dia, mes, año

def DiasDelMes(mes, año):
    '''
    Recibe un mes y un año y nos dicee los días de ese mes en ese año.

    Args:
    mes (int): El mes.
    año (int): El año.
    
    Return:
    int: El número de días del mes.
    '''
    
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    elif mes == 2:
        if EsBisiesto(año):
            return 29
        else:
            return 28
    else:
        return 31
    
def EsBisiesto(año):
    '''
    Recibe un año y nos dice si es bisiesto.
    
    Args:
    año (int): El año.
    
    Return:
    bool: True si es bisiesto, False si no lo es.
    '''
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False
    
def Calcular_Dia_Juliano(dia, mes, año):
    '''
    Recibe una fecha y devuelve el día juliano
    
    Args:
    dia (int): El día deel mes.
    mes (int): El mes.
    año (int): El año.
    
    Return:
    int: El día juliano.
    '''
    
    dia_juliano = dia
    for m in range(1, mes):
        dia_juliano += DiasDelMes(m, año)
    
    return dia_juliano

def main():
    '''
    Programa principal que calcula el dia juliano correspondiente a una fecha dada.
    '''
    while True:
        print("\nMenú:")
        print("1. Calcular día juliano")
        print("2. Salir")
        opcion = input("Elige una opción (1/2): ")

        if opcion == '1':
            dia, mes, año = LeerFecha()
            dia_juliano = Calcular_Dia_Juliano(dia, mes, año)
            print(f"\nLa fecha {dia}/{mes}/{año} corresponde al día juliano {dia_juliano}.")
        
        elif opcion == '2':
            print("\nSaliendo del programa...")
            break
        
        else:
            print("\nOpción no válida, por favor elige una opción válida.")

if __name__ == "__main__":
    main()