'''
Enunciado:

1. Crear una función `EscribirCentrado`, que reciba como parámetro un texto 
y lo escriba centrado en pantalla (suponiendo una anchura de 80 columnas; 
pista: deberás escribir 40 - longitud/2 espacios antes del texto). 
Además, subraya el mensaje utilizando el carácter `=`.

Solución:
'''

def EscribirCentrado(texto):
    
    # Ancho de la pantalla
    ancho = 80
    
    # Espacios en blanco necesarios
    espacios = (ancho - len(texto))//2
    
    # Imprimimos
    print(" " * espacios, texto)
    print(" " * espacios, "=" * len(texto))
    
def main():
    text = "Hola a todos los presentes"

    EscribirCentrado(text)
    
if __name__ == "__main__":
    main()