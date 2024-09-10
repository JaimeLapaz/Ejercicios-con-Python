'''
Enunciado:

17. **Diccionario Anidado**: Trabaja con un diccionario anidado que represente datos 
de una tienda, como productos y precios.

Solución:
'''

# Función para mostrar todos los productos y precios
def mostrar_productos(tienda: dict) -> None:
    '''
    Esta función recoge el diccionario y lo imprime por pantalla.
    
    Args:
    tienda (dict): Diccionario anidado con productos y precios.
    
    Return:
    None
    '''
    for categoria, productos in tienda.items():
        print(f"\nCategoría: {categoria}")
        for producto, precio in productos.items():
            print(f"  {producto}: ${precio:.2f}")

# Función para agregar un nuevo producto a una categoría
def agregar_producto(tienda: dict, categoria: str, producto: str, precio: float) -> dict:
    '''
    Esta función agrega un nuevo producto a una categoría.
    
    Args:
    tienda (dict): Diccionario anidado con productos y precios.
    categoria (str): Categoría a la que se agregará el producto.
    producto (str): Nombre del producto a agregar.
    precio (float): Precio del producto a agregar.
    
    Return:
    dict: Diccionario anidado con el nuevo producto.
    '''
    if categoria in tienda:
        tienda[categoria][producto] = precio
        print(f"\nProducto '{producto}' agregado a la categoría '{categoria}' con precio ${precio:.2f}.")
        return tienda
    else:
        print(f"\nLa categoría '{categoria}' no existe en la tienda.")

# Función para eliminar un producto de una categoría
def eliminar_producto(tienda: dict, categoria: str, producto: str) -> dict:
    '''
    Esta función elimina un producto de una categoría.
    
    Args:
    tienda (dict): Diccionario anidado con productos y precios.
    categoria (str): Categoría de la que se eliminará el producto.
    producto (str): Nombre del producto a eliminar.
    
    Return:
    dict: Diccionario anidado sin el producto eliminado.
    '''
    if categoria in tienda and producto in tienda[categoria]:
        del tienda[categoria][producto]
        print(f"\nProducto '{producto}' eliminado de la categoría '{categoria}'.")
        return tienda
    else:
        print(f"\nEl producto '{producto}' no existe en la categoría '{categoria}'.")

# Función para actualizar el precio de un producto
def actualizar_precio(tienda: dict, categoria: str, producto: str, nuevo_precio: float) -> dict:
    '''
    Esta función actualiza el precio de un producto.
    
    Args:
    tienda (dict): Diccionario anidado con productos y precios.
    categoria (str): Categoría del producto a actualizar.
    producto (str): Producto a actualizar.
    nuevo_precio (float): Nuevo precio del producto.
    
    Return:
    dict: Diccionario anidado con el precio actualizado.
    '''
    if categoria in tienda and producto in tienda[categoria]:
        tienda[categoria][producto] = nuevo_precio
        print(f"\nPrecio del producto '{producto}' actualizado a ${nuevo_precio:.2f}.")
        return tienda
    else:
        print(f"\nEl producto '{producto}' no existe en la categoría '{categoria}'.")

if  __name__ == "__main__":
    # Definimos el diccionario anidado de la tienda
    tienda = {
        'alimentos': {
            'manzanas': 1.20,
            'pan': 1.50
        },
        'tecnologia': {
            'auriculares': 30.99,
            'teclado': 25.00
        },
        'ropa': {
            'camiseta': 12.99,
            'pantalones': 25.50
        }
    }

    # Ejemplo de uso:
    # Mostrar los productos actuales en la tienda
    mostrar_productos(tienda)

    # Agregar un nuevo producto a la categoría 'alimentos'
    tienda = agregar_producto(tienda, 'alimentos', 'leche', 1.80)

    # Eliminar un producto de la categoría 'ropa'
    tienda = eliminar_producto(tienda, 'ropa', 'camiseta')

    # Actualizar el precio de un producto en la categoría 'tecnologia'
    tienda = actualizar_precio(tienda, 'tecnologia', 'teclado', 27.50)

    # Mostrar los productos después de las modificaciones
    mostrar_productos(tienda)