"""Diccionario de preguntas, alternativas y respuestas (1 es la correcta)"""

preguntas_basicas = {
    'pregunta_1': {'enunciado':['¿En qué año nació Isaac Asimov?'],
    'alternativas': [['1919', 0], 
                     ['1920', 1], 
                     ['1921', 0], 
                     ['1922', 0]]},
    'pregunta_2': {'enunciado':['¿Cuál es el nombre del robot protagonista de muchas de las historias de Asimov?'],
    'alternativas': [['R2-D2', 0], 
                     ['HAL 9000', 0], 
                     ['C-3PO', 0], 
                     ['Robbie', 1]]},
    
    'pregunta_3': {'enunciado':['¿Cuál es la primera ley de la robótica según Asimov?'],
    'alternativas': [['Un robot no puede lastimar a un ser humano o, por inacción, permitir que un ser humano sufra daño', 1], 
                     ['Un robot no puede lastimar a un ser humano ni, por inacción, permitir que un ser humano sufra daño a menos que esto entre en conflicto con la Tercera Ley.', 0], 
                     ['Un robot no puede desobedecer las órdenes dadas por un ser humano, excepto si esto entra en conflicto con la Primera o Segunda Ley.', 0], 
                     ['Un robot no puede lastimar a la humanidad o, por inacción, permitir que la humanidad sufra daño.', 0]]}
}

preguntas_intermedias = {
    'pregunta_1': {'enunciado':['¿Cuál es el título de la trilogía de Asimov compuesta por las novelas "Fundación", "Fundación e imperio" y "Segunda Fundación"?'],
    'alternativas': [['Trilogía del Robot', 0], 
                     ['Ciclo de Trántor', 0], 
                     ['Ciclo de Gaia', 0], 
                     ['Trilogía de la Fundación', 1]]},

    'pregunta_2': {'enunciado':['¿Qué libro de Asimov describe las leyes de la robótica?'],
    'alternativas': [['Yo, robot', 1], 
                     ['Los propios dioses', 0], 
                     ['El fin de la eternidad', 0], 
                     ['El sol desnudo', 0]]},
    
    'pregunta_3': {'enunciado':['¿Cuál es el título de la colección de cuentos de Asimov que incluye "Yo, robot"?'],
    'alternativas': [['Visiones de robot', 1], 
                     ['Cuentos de robots', 0], 
                     ['La edad de oro', 0], 
                     ['El gran libro de la ciencia ficción', 0]]}
}

preguntas_avanzadas = {
    'pregunta_1': {'enunciado':['¿Cuál es el nombre del personaje principal en la serie de novelas de Asimov "El Ciclo de la Fundación"?'],
    'alternativas': [['Elijah Baley', 0], 
                     ['Hari Seldon', 1], 
                     ['R. Daneel Olivaw', 0], 
                     ['Golan Trevize', 0]]},

    'pregunta_2': {'enunciado':['¿En qué historia de Asimov aparece por primera vez el concepto de las Tres Leyes de la Robótica?'],
    'alternativas': [['Robbie', 0], 
                     ['Corriente', 0], 
                     ['Yo, robot', 1], 
                     ['Pequeño robot perdido', 0]]},
    
    'pregunta_3': {'enunciado':['¿Cuál es la última novela de la serie "El Ciclo de la Fundación" escrita por Asimov?'],
    'alternativas': [['Preludio a la Fundación', 0], 
                     ['Hacia la Fundación', 1], 
                     ['Fundación y Tierra', 0], 
                     ['Fundación y Caos', 0]]}
}

pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}