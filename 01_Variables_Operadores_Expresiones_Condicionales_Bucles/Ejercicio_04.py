'''
Enunciado:

4. Hacer un programa que solicite una edad e imprima "Es mayor" si es mayor de edad, sino que imprima "Es menor".

Solución:
'''

edad = int(input("Introduce tu erad: "))

if edad < 0:
    print("La edad no puede ser negativa")
elif edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")