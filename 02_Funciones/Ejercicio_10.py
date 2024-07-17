'''
Enunciado:

10. Escribir dos funciones que permitan calcular:
    - La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
    - La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
    - Escribir un programa principal con un menú donde se pueda elegir la opción 
    de convertir a segundos, convertir a horas, minutos y segundos, o salir del programa.
    
Solución:
'''

def convertir_segundos(horas, minutos, segundos):
    '''
    Convieerte un tiempo dado en horas, minutos y segundos a la cantidad total en segundos.
    
    Args:
    horas (int): Cantidad de horas.
    minutos (int): Cantidad de minutos.
    segundos (int): Cantidad de segundos.
    
    Return:
    int: Cantidad total de segundos.
    '''
    
    total_segundos = horas*3600 + minutos*60 + segundos
    return total_segundos

def convertir_hms(segundos):
    '''
    Convierte una cantidad dada de segundos a horas, minutos y segundos.
    
    Args:
    segundos (int): Cantidad de segundos.
    
    Return:
    tuple: Cantidad de horas, minutos y segundos.
    '''
    
    horas = segundos // 3600
    segundos = segundos % 3600
    minutos = segundos // 60
    segundos = segundos % 60
    return horas, minutos, segundos

def main():
    '''
    Programa principal con un menú para elegir la opción de convertir a segundos, convertir a horas, minutos y segundos, o salir del programa.
    '''
    
    while True:
        print("\nMenú:")
        print("1. Convertir a segundos")
        print("2. Convertir a horas, minutos y segundos")
        print("3. Salir")
        opcion = input("Elige una opción (1/2/3): ")

        if opcion == '1':
            horas = int(input("Ingresa horas: "))
            minutos = int(input("Ingresa minutos: "))
            segundos = int(input("Ingresa segundos: "))
            total_segundos = convertir_segundos(horas, minutos, segundos)
            print(f"\n{horas} horas, {minutos} minutos y {segundos} segundos son {total_segundos} segundos.")
        
        elif opcion == '2':
            segundos_totales = int(input("Ingresa la cantidad de segundos: "))
            horas, minutos, segundos = convertir_hms(segundos_totales)
            print(f"\n{segundos_totales} segundos son {horas} horas, {minutos} minutos y {segundos} segundos.")
        
        elif opcion == '3':
            print("\nSaliendo del programa...")
            break
        
        else:
            print("Opción no válida, por favor elige una opción válida.")

if __name__ == "__main__":
    main()
    