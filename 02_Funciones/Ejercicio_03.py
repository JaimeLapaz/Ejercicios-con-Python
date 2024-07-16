'''
Enunciado:

3. Crear una función que calcule la temperatura media de un día a partir 
de la temperatura máxima y mínima. Crear un programa principal que utilice esta función, 
pidiendo la temperatura máxima y mínima de cada día y mostrando la media. 
El programa pedirá el número de días que se van a introducir.

Solución:
'''

def TemperaturaMedia(maxima, minima):
    return (maxima + minima) / 2

def main():
    
    # Pedimos el número de días
    num_dias = int(input("Introduce el número de días: "))
    
    # Pedimos las temperaturas y calculamos sus media en cada uno de los días
    for i in range(num_dias):
        print(f"Día {i+1}")
        maxima = float(input("Introduce la temperatura máxima: "))
        minima = float(input("Introduce la temperatura mínima: "))
        print("La temperatura media es: ", TemperaturaMedia(maxima, minima))
        
if __name__ == "__main__":
    main()