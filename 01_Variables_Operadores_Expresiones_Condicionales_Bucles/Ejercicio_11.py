'''
Enunciado:

11. Hacer un programa donde se muestre el siguiente dibujo:

    
    *  *  *  *  *  *  *  *  *  *
    *                          *
    *                          *
    *                          *
    *  *  *  *  *  *  *  *  *  *
    
Solución:
'''

filas = 5
columnas = 10

for i in range(filas):
    if i == 0 or i == filas - 1:
        print("* " * columnas)
    else:
        print("*" + " " *((columnas - 2) * 2 + 1) + "*")