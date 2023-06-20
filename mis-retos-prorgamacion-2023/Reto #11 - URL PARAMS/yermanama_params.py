"""
Dada una URL con parámetros, crea una función que obtenga sus valores.
No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
los parámetros serían ["2023", "0"]
"""

url = "https://retosdeprogramacion.com?year=2023&challenge=0"

primera_descomposicion = url.split("?")
print(primera_descomposicion)

segunda_descomposicion = primera_descomposicion[1].split("&")
print(segunda_descomposicion)

parametros = []
for parametro in segunda_descomposicion:
    parametros.append(parametro.split("=")[1])

print(parametros)