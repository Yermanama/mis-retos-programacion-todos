"""
Dada una URL con parámetros, crea una función que obtenga sus valores.
No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
los parámetros serían ["2023", "0"]
"""

#Ahora lo vamos a hacer con una librería

from urllib.parse import urlparse, parse_qs

url = "https://retosdeprogramacion.com?year=2023&challenge=0"

url_components = urlparse(url)

print(url_components)

cadena_consulta = url_components.query

print(cadena_consulta)

parametros_consulta = parse_qs(cadena_consulta)

print(list(parametros_consulta.values()))