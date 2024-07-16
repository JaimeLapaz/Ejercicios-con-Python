'''
Enunciado:

5. Crear una función `calcularMaxMin` que reciba una lista con valores numéricos y 
devuelva el valor máximo y el mínimo. Crear un programa que pida números por teclado y 
muestre el máximo y el mínimo utilizando esta función.

Solución:
'''

def calcularMaxMin(lista):
    maximo = lista[0]
    minimo = lista[0]
    for i in lista:
        # Buscamos el valor máximo
        if i > maximo:
            maximo = i
            
        # Buscamos el valor mínimo
        if i < minimo:
            minimo = i
    
    return maximo, minimo

def main():
    
    # Inicializamos la lista vacía
    lista = []
    while True:
        # Pedimos números y damos el parámetro de parada
        num = int(input("Ingrese un número, escribe 0 para terminar: "))
        
        # Comprobamos la condición de parada
        if num == 0:
            break
        
        # Añadimos el número a la lista
        lista.append(num)
    
    # Calculamos el máximo y el mínimo
    maximo, minimo = calcularMaxMin(lista)
    
    # Imprimimos por pantalla
    print(f"\nEl máximo es {maximo}\nEl mínimo es {minimo}")

if __name__ == "__main__":
    main()