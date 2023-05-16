"""
    Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
    El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
    gane cada punto del juego.
    - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
    - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
15 - Love
30 - Love
30 - 15
30 - 30
40 - 30
Deuce
Ventaja P1
Ha ganado el P1
Si quieres, puedes controlar errores en la entrada de datos.
Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
"""


p1_puntuacion = 0
p2_puntuacion = 0
secuencia = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

def conversor_secuencia_a_puntos(secuencia, p1_puntuacion, p2_puntuacion):
    imprimir_puntuaciones(p1_puntuacion, p2_puntuacion)
    for punto in secuencia:
        if punto == "P1":
            p1_puntuacion = incremento_puntuacion(p1_puntuacion, p2_puntuacion, jugador="P1")
            imprimir_puntuaciones(p1_puntuacion, p2_puntuacion)
        else:
            p2_puntuacion = incremento_puntuacion(p2_puntuacion, p1_puntuacion, jugador="P2")

def incremento_puntuacion(puntuacion_a_subir, puntuacion_rival, jugador):
    if puntuacion_a_subir == 0:
        puntuacion_a_subir = 15
        return puntuacion_a_subir
    elif puntuacion_a_subir == 15:
        puntuacion_a_subir = 30
        return puntuacion_a_subir
    elif puntuacion_a_subir == 30:
        puntuacion_a_subir = 45
        return puntuacion_a_subir
    elif puntuacion_a_subir == 45:
        if puntuacion_rival == 45:
            puntuacion_a_subir == f'Ventaja jugador {jugador}'
        else:
            puntuacion_a_subir = f'Ha ganado jugador {jugador}'



def imprimir_puntuaciones(punt1, punt2):
    if punt1 == 0 and punt2 == 0:
        print("Love-Love")
    elif 
