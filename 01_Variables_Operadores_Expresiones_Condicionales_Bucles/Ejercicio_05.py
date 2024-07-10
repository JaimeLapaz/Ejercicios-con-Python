'''
Enunciado:

5. Hacer un programa que solicite un color por teclado e imprima 
"Puede pasar" si el color ingresado es verde, 
"Precaución" si es amarillo, 
"No pasar" si es rojo 
o "Color inválido" si es cualquier otro.

Solución:
'''

color = input("Ingrese un color: ")

if color.lower() == "verde":
    print("Puede pasar.")
elif color.lower() == "amarillo":
    print("Precaución.")
elif color.lower() == "rojo":
    print("No pasar.")
else:
    print("Color inválido.")