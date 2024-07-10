'''
Enunciado:

12. Hacer un programa que muestre el siguiente dibujo:

    *
    *    *
    *    *    *
    *    *    *    *
    *    *    *    *    *
    
Solución:
'''


filas = 5

for i in range(filas):
    print("* " * (i+1))