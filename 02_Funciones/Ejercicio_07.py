'''
Enunciado:

7. Crear una subrutina llamada `Login`, que recibe un nombre de usuario y una contraseña 
y te devuelve Verdadero si el nombre de usuario es "usuario1" y la contraseña es "asdasd". 
Además, recibe el número de intentos que se ha intentado hacer login y si no se ha podido 
hacer login incremente este valor. Crear un programa principal donde se pida un nombre de usuario y 
una contraseña e intente hacer login, solamente tenemos tres oportunidades para intentarlo.

Solución:
'''

def Login(usuario, contrasena, intentos):
    '''
    Verifica si el nombre de usuario y la contraseña son correctos.
    
    Args:
        usuario (str): Nombre de usuario.
        contrasena (str): Contraseña.
        intentos (int): Número de intentos realizados.

    Returns:
        bool: Verdadero si el login es correcto, Falso en caso contrario.
        int: Número de intentos incrementado si el login es incorrecto.
    '''
    usuario_correcto = "usuario1"
    contrasena_correcta = "asdasd"
    
    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        return True, intentos
    else:
        intentos += 1
        return False, intentos

def main():
    intentos = 0
    max_intentos = 3
    
    while intentos < max_intentos:
        usuario = input("\nIntroduce el nombre de usuario: ")
        contrasena = input("Introduce la contraseña: ")
        
        es_correcto, intentos = Login(usuario, contrasena, intentos)
        
        if es_correcto:
            print("\nLogin exitoso.")
            break
        else:
            print("\nNombre de usuario o contraseña incorrectos.")
            if intentos < max_intentos:
                print(f"Intentos restantes: {max_intentos - intentos}")
    
    if intentos == max_intentos:
        print("\nHas agotado todos los intentos. Acceso denegado.")

if __name__ == "__main__":
    main()