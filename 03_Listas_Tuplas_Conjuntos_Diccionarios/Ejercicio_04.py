'''
Enunciado:

4. Suponer una lista con datos de las compras hechas por clientes de una empresa 
a lo largo de un mes, la cual contiene tuplas con información de cada venta: 
(cliente, día del mes, monto, domicilio del cliente). Ejemplo:

   ```python
   [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), 
   ("Jorge Russo", 7, 699, "Mirasol 218"), 
   ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), 
   ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), 
   ("Jorge Russo", 15, 958, "Mirasol 218")]
   ```

Escribir una función que reciba como parámetro una lista con el formato mencionado 
anteriormente y retorne los domicilios de cada cliente al cual se le debe enviar 
una factura de compra. Notar que cada cliente puede haber hecho más de una compra 
en el mes, por lo que la función debe retornar una estructura que contenga cada 
domicilio una sola vez.

Solución:
'''

from typing import List, Set, Tuple

def obtener_domicilio_factura(compras: List[Tuple[str, int, float, str]]) -> Set[str]:
    """
    Recibe una lista de tuplas con información de ventas y retorna un conjunto con los domicilios
    a los que se debe enviar una factura de compra.

    Args:
    compras (List[Tuple[str, int, float, str]]): Lista de ventas en el formato (cliente, día, monto, domicilio).

    Returns:
    Set[str]: Conjunto con los domicilios únicos de los clientes.
    """
    domicilios = {}
    
    for cliente, _, _, domicilio in compras:
        domicilios[cliente] = domicilio
        
    return set(domicilios.values())

def main():
    # Ejemplo de uso
    compras_mes = [
        ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
        ("Jorge Russo", 7, 699, "Mirasol 218"),
        ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
        ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
        ("Jorge Russo", 15, 958, "Mirasol 218")
    ]
    
    domicilios_facturas = obtener_domicilio_factura(compras_mes)
    print(domicilios_facturas)

if __name__ == "__main__":
    main()