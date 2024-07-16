'''
Enunciado:

6. Diseñar una función que calcule el área y el perímetro de una circunferencia. 
Utiliza esta función en un programa principal que lea el radio de una circunferencia y 
muestre su área y perímetro.

Solución:
'''
# Importamos el número pi
from math import pi


def PerimetroAreaCircunferencia(radio):
    # Calculamos el área
    area = round(pi * (radio ** 2), 2)
    
    # Calculamos el perímetro
    perimetro = round(2 * pi * radio, 2)
    
    return area, perimetro

def main():
    # Pedimos el radio
    radio = float(input("Introduce el radio de la circunferencia: "))
    
    area, perimetro = PerimetroAreaCircunferencia(radio)
    
    print(f"\nEl área de la circunferencia es: {area}\nEl perímetro de la circunferencia es: {perimetro}")
    
if __name__ == "__main__":
    main()