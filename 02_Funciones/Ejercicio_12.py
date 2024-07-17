'''
Enunciado:

12. Vamos a mejorar el ejercicio anterior haciendo una función para validar la fecha, 
de tal forma que al leer una fecha se asegure que es válida.

Solución:
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
    if ValidarFecha(dia, mes, año):
        return dia, mes, año
    else:
        print('La fecha introducida no es válida.')

def ValidarFecha(dia, mes, año):
    '''
    Valida que la fecha sea válida.
    
    Args:
    dia (int): Día de la fecha.
    mes (int): Mes de la fecha.
    año (int): Año de la fecha.
    
    Return:
    bool: True si la fecha es válida, False en caso contrario.
    '''
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > DiasDelMes(mes, año):
        return False
    
    return True

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