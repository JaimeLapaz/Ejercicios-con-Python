'''
Enunciado:

4. Crear una función `ConvertirEspaciado` que reciba como parámetro un texto 
y devuelva una cadena con un espacio adicional tras cada letra. 
Por ejemplo, "Hola, tú" devolverá "H o l a , t ú". 
Crear un programa principal donde se use dicha función.

Solución:
'''

def ConvertirEspaciado(text):
    texto = ""
    for i in text:
        if i != " ":
            texto += i + " "
        else:
            texto += i
            
    return texto

def main():
    
    text = "Hola, tú"
    
    print(ConvertirEspaciado(text))
    
if __name__ == "__main__":
    main()