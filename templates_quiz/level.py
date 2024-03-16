def choose_level(n_pregunta, p_level):
	"""
	Esta función toma dos argumentos: n_pregunta, que representa el número de la pregunta, 
	y p_level, que es un valor que indica el nivel de preguntas que quieres dividir.
	"""
	if n_pregunta <= p_level:
		level = "basicas"
	elif n_pregunta <= 2*p_level:
		level= "intermedias"
	else:
		level = "avanzadas"
	return level

