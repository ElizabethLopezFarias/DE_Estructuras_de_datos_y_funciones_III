import preguntas as p

def print_pregunta(enunciado, alternativas):
    """
    Esta función toma dos argumentos: enunciado, que es una lista que contiene el enunciado de la pregunta, 
    y alternativas, que es una lista de listas que contiene las diferentes opciones de respuesta.
    """
    # Imprime el enunciado de la pregunta
    print (enunciado[0], "\n")
    # Diccionario que asigna letras a las opciones
    opciones = {
        0:"A.",
        1:"B.",
        2:"C.",
        3:"D."
    }
    # Itera sobre las alternativas
    for i, alternativa in enumerate(alternativas):
        print (opciones[i], alternativa[0])    
    
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
