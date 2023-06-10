"""
 Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
 y retorne lo siguiente:
  - "X" si han ganado las "X"
 - "O" si han ganado los "O"
 - "Empate" si ha habido un empate
 - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
  O si han ganado los 2.
Nota: La matriz puede no estar totalmente cubierta.
Se podría representar con un vacío "", por ejemplo.
"""

#Primero vamos a verificar que la matriz que nos pasan es válida

def es_valida(matriz):
    x_contador = 0
    o_contador = 0 
    for fila in matriz:
        for char in fila:
            if char == "X":
                x_contador += 1
            elif char == "O":
                o_contador += 1
            elif char != "":
                return False # Esto significa que hay algo incorrecto en la matriz y hay que descartarla
    if abs(x_contador - o_contador) > 1: # Esto siginifica que la proporción es incorrecta, debe de haber el mismo número o sólo una más
        return False
    if len(matriz) != 3 or any(len(fila) != 3 for fila in matriz): #Si la longitud de la matriz es mayor a la que queremos o si alguna de las fials también supera la longitud 3
        return False
    return True

# Ahora tenemos que ver quien gana, para ello debemos de comprobar 8 posibles escenarios

def quien_gana(matriz):
    # comprobamos las filas
    for fila in matriz:
        if fila [0] == fila[1] == fila[2] != "":
            return fila[0]
    # comprobamos las columnas
    for numero_casilla in range(3):
        if matriz[0][numero_casilla] == matriz[1][numero_casilla] == matriz[2][numero_casilla] != "":
            return matriz[0][numero_casilla]
    #comprobamos las diagonales
    if matriz[0][0] == matriz[1][1] == matriz[2][2] != "":
        return matriz[0][0]
    if matriz[0][2] == matriz[1][1] == matriz[2][0] != "":
        return matriz[0][2]
    return None

# Aplicamos las dos funciones anteriores en la lógica del juego

def resultado_juego(matriz):
    if es_valida(matriz):
        ganador = quien_gana(matriz)
    else:
        return "La matriz proporcionada no es válida por lo que no podemos continuar con el juego"
    if ganador is not None:
        return ganador 
    if any("" in fila for fila in matriz):
        return "El juego todavía no ha terminado"
    return "Empate"

# Ejemplo de uso:
matriz = [
    ["X", "O", "X"],
    ["O", "X", ""],
    ["O", "", "X"],
]
print(resultado_juego(matriz))