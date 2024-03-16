import preguntas as p


def verificar(alternativas, eleccion):
    """
    Esta función toma dos argumentos: alternativas, que es una lista que contiene las opciones posibles 
    (cada una representada como una tupla que consiste en la opción y un indicador de si es correcta o no), 
    y eleccion, que es la letra de la opción elegida por el usuario (por ejemplo, 'a', 'b', 'c', 'd').
    
    """
    #devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c','d'].index(eleccion)
    # Comprueba si la opción elegida es la correcta
    if alternativas[eleccion][1]==1:
        correcto = True
    else:
        correcto = False

     # Devuelve True si la elección es correcta, False si no lo es    
    return correcto



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    print(verificar(pregunta['alternativas'], respuesta))






