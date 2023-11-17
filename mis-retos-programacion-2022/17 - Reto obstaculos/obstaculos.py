"""
Crea una función que evalúe si un/a atleta ha superado correctamente una
carrera de obstáculos.
- La función recibirá dos parámetros:
     - Un array que sólo puede contener String con las palabras
       "run" o "jump"
     - Un String que represente la pista y sólo puede contener "_" (suelo)
       o "|" (valla)
- La función imprimirá cómo ha finalizado la carrera:
     - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
       será correcto y no variará el símbolo de esa parte de la pista.
     - Si hace "jump" en "_" (suelo), se variará la pista por "x".
     - Si hace "run" en "|" (valla), se variará la pista por "/".
- La función retornará un Boolean que indique si ha superado la carrera.
Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""
def ha_superado(obstaculos: str, atleta: list): 
    obstaculos = [obstaculo for obstaculo in obstaculos]
    diccionario = {}
    for obstaculo, accion in zip(obstaculos, atleta):
        if obstaculo not in diccionario:
            diccionario[obstaculo] = []
        diccionario[obstaculo].append(accion)
    nuevo_diccionario = {}
    for clave, valor in diccionario.items():
        if clave == "_" and "jump" in valor:
            nuevo_diccionario["x"] = valor
        elif clave == "|" and "run" in valor:
            nuevo_diccionario["/"] = valor
        elif clave == "_" and "run" in valor:
            nuevo_diccionario["_"] = valor
        elif clave == "_" and "jump" in valor:
            nuevo_diccionario["_"] = valor
    print(nuevo_diccionario.keys())
    if "/" in nuevo_diccionario.keys() or "x" in nuevo_diccionario.keys():
        return False
    else: return True

pista1 = "_|_|_|_"
atleta1 = ["run", "jump", "run", "jump", "run"]
print(ha_superado(pista1, atleta1))

pista2 = "_|_|_|_"
atleta2 = ["run", "run", "jump", "run","run", "jump", "run"]
print(ha_superado(pista2, atleta2))
