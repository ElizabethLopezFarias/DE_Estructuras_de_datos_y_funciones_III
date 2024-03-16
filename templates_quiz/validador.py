
def validate(opciones, eleccion):
    """
    Valida si la elección está dentro del conjunto de opciones.

    Args:
        opciones (list): Lista de opciones válidas.
        eleccion: Elección ingresada por el usuario.

    Returns:
        str: La opción ingresada por el usuario si es válida.
    """
    while True:
        if eleccion in opciones:
            return eleccion
        else:
            eleccion = input(f'Opción no válida. Ingrese una de las opciones válidas ({", ".join(opciones)}): ')
            #eleccion = input('Opción no válida. Ingrese una de las opciones válidas: a, b, c, d')

# if __name__ == '__main__':
#     opciones_validas = ["a", "b", "c", "d"]
#     eleccion = input('Ingresa una Opción: ').lower()
#     opciones = ['a','b','c','d'] # opciones válidas
#     # Ejecuta la función para validar si la respuesta del usuario es válida
#     opcion_validada = validate(opciones, eleccion)
#     print(f"Opción válida seleccionada: {opcion_validada}") #muestra la opción seleccionada
    
