'''
Enunciado:

7. Hacer un programa que cuente del 1 al 100 inclusive e imprima sólo los números pares.

Solución:
'''
print("Los números pares del 1 al 100 son: ")
for i in range(1,101):
    if i % 2 == 0:
        print(i)