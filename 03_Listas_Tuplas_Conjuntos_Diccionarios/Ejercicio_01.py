'''
Enunciado:

1. Realiza los siguientes apartados:

- A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. 
Finalizar al ingresar el número 0, el cual no debe guardarse.

- B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, 
eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.

- C) Recorrer la lista para imprimir la sumatoria de todos los elementos.

- D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean 
menores que el número dado. Imprimir esta nueva lista, iterando por ella.

- E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, 
cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. 
Por ejemplo, si la lista original es `[5, 16, 2, 5, 57, 5, 2]` la nueva lista contendrá: `[(5, 3), (16, 1), (2, 2), (57, 1)]`.

Solución:
'''

def main():
    # A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista.
    # Inicializamos la lista
    lista = []
    while True:
        # Pedimos los números a los usuarios.
        num = int(input("Ingrese un número (0 para parar): "))
        if num == 0:
            break
        
        # Añadimos los números a la lista   
        lista.append(num)
    
    # B) Solicitamos un número al usuario para eliminar.
    num = int(input("Ingrese un número para eliminar: "))
    try:
        # Eliminamos el primer elemento que coincida con el número ingresado.
        lista.remove(num)
    except ValueError:
        print("No se encontró el número en la lista")
    
    print(f"Lista sin el número {num} es: {lista}")
    
    # C) Recorrer la lista para que se haga la sumatoria de todos los elementos iterando la lista
    # Inicializamos la suma
    suma = 0
    # Iteramos la lista
    for i in lista:
        # Vamos sumando
        suma += i
    
    print(f"La suma de los elementos de la lista es: {suma}")
    
    # D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean 
    # menores que el número dado. Imprimir esta nueva lista, iterando por ella.
    # Pedimos el número al usuario
    num2 = int(input("Ingrese un número: "))
    # Inicializamos la lista
    lista_menor = [num for num in lista if num < num2]
    
    # Imprimimos la lista nueva.
    print(f"Los elementos menores que {num2} son:")
    for i in lista_menor:
        print(i)
    
    # E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos,
    # cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. 
    # Por ejemplo, si la lista original es `[5, 16, 2, 5, 57, 5, 2]` la nueva lista contendrá: `[(5, 3), (16, 1), (2, 2), (57, 1)]`.
    ocurrencias = {}
    for i in lista:
        if i in ocurrencias:
            ocurrencias[i] += 1
        else:
            ocurrencias[i] = 1
    lista_tuplas = [(num, count) for num, count in ocurrencias.items()]
    
    print("Lista de tuplas (número, cantidad de ocurrencias):", lista_tuplas)
    
if __name__ == "__main__":
    main()
