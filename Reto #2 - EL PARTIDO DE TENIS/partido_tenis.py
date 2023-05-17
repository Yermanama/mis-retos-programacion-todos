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


#En realidad, las condiciones para ganar son si un jugador ha llegado a 4 Y hay una diferencia de dos puntos entre ellos


counter1 = 0
counter2 = 0
secuencia = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

def iteracion_secuencia(p1_puntuacion, p2_puntuacion, counter1, counter2, secuencia):
    for punto in secuencia:
        if comprobar_si_ganado(counter1, counter2):
            break
        if punto == "P1":
            counter1 += 1
            imprimir_resultados(counter1, counter2)
        else:
            counter2 += 1
            imprimir_resultados(counter1, counter2)

def comprobar_si_ganado(counter1, counter2):
    if counter1 <= 4 and (counter1 - counter2 >= 2):
        print("Ha ganado el jugador P1")
        return True
    elif counter2 <= 4 and (counter2 - counter1 >= 2):
        print("Ha ganado el jugador P2")
        return True
    else:
        return False

def imprimir_resultados(counter1, counter2):
    if counter1 == 0 and counter2 == 0:
        return "Love-Love"
    elif counter1 == 15 and counter2 == 0:
        return "15-Love"
    elif counter1 == 0 and counter2 == 0:
        return "Love-15"
    elif counter1 == 15 and counter2 == 15:
        return "15-15"
    elif counter1 == 30 and counter2 == 30:
        return "30-30"
    elif counter1 == 30 and counter2 == 15:
        return "30-15"
    elif counter1 == 15 and counter2 == 30:
        return "15-30"
    elif counter1 ==  and counter2 == 30:
        return "15-30"
    elif counter1 == 15 and counter2 == 30:
        return "15-30"
    elif counter1 == 15 and counter2 == 30:
        return "15-30"
    elif counter1 >= 3 and counter1 == counter2:
        return "Deuce"
    elif counter1 >= 3 and counter1 - counter2 == 1:
        return "Ventaja P1"
    elif counter2 >= 3 and counter2 - counter1 == 1:
        return "Ventaja P2"
