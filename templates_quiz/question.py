import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}

def choose_q(dificultad):
    """
    Permite al usuario elegir una pregunta según la dificultad.

    Args:
        dificultad (str): La dificultad de la pregunta ('basicas', 'intermedias' o 'avanzadas').

    Returns:
        tuple: El enunciado de la pregunta y las alternativas mezcladas.
    """
    #escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]
    
    # opciones desde ambiente global
    global opciones
    # escoger una pregunta
    n_elegido = random.choice(opciones[dificultad])
    # eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido)
    # escoger enunciado y alternativas mezcladas
    pregunta = preguntas[f"pregunta_{n_elegido}"]
    alternativas = shuffle_alt(pregunta)  # Mezcla las alternativas
    
    #retorna el enunciado y las alternativas correspondientes
    return pregunta['enunciado'], alternativas
