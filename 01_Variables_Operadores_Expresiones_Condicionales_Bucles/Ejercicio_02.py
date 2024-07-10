'''
Enunciado:

2. Hacer un programa que solicite por teclado dos números y muestre la suma, la resta, la multiplicación y la división de esos números.

Solución:
'''

num1 = float(input("Introduce dos numeros. \nPrimer número: "))
num2 = float(input("Segundo número: "))

print("La suma es: ", num1 + num2)

print("La resta es: ", num1 - num2)

print("La multiplicación es: ", num1*num2)

if num2 == 0:
    print("La división no se puede realizar. No se puede dividir por 0")
else:
    print("La división es: ", round(num1/num2, 2))