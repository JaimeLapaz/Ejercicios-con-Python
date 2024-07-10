'''
Enunciado:

8. Hacer un programa que cuente del 1 al 100 inclusive e imprima los números que son 
divisibles por 2 y por 5.

Solución:
'''

print("Los numeros entre 1 y 100 que son divisibles por 2 y por 5 son:")
for i in range(1,101):
    if i % 2 == 0 and i % 5 == 0:
        print(i)