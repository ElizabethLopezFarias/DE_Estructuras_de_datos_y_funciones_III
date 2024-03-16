import preguntas as p
import random

def shuffle_alt(pregunta):
    """
    Mezcla las alternativas de una pregunta dada.

    Args:
        question (dict): Un diccionario que contiene la pregunta, el nivel y las alternativas.

    Returns:
        list: Alternativas mezcladas.
    """
    # Extrae las alternativas de la pregunta
    alternativas = pregunta.get("alternativas", [])

    # Mezcla las alternativas
    random.shuffle(alternativas)

    return pregunta['alternativas']

if __name__ == '__main__':
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1'])) 
    # a modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]