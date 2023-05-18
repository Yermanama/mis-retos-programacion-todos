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



secuencia_prueba = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]


def iteracion_secuencia(secuencia):
    counter1 = 0
    counter2 = 0
    for punto in secuencia:
        if punto == "P1":
            counter1 += 1
        elif punto == "P2":
            counter2 += 1

        if comprobar_si_ganado(counter1, counter2):
            break

        print(imprimir_resultados(counter1, counter2))




def comprobar_si_ganado(counter1, counter2):
    if counter1 >= 4 and (counter1 - counter2 >= 2):
        print("Ha ganado el jugador P1")
        return True
    elif counter2 >= 4 and (counter2 - counter1 >= 2):
        print("Ha ganado el jugador P2")
        return True
    else:
        return False

def imprimir_resultados(counter1, counter2):
    #Primero vamos a hacer un diccionario con los puntos pasados a lo que queremos traducir
    puntos_a_terminos = {0:"Love", 1:"15", 2: "30", 3:"40"}

    #Ahora vamos a gestionar las excepciones a los puntos de arriba
    if counter1 >= 3 and counter1 == counter2:
        return "Deuce"
    elif counter1 >= 4 and counter1-counter2 == 1:
        return "Ventaja para P1"
    elif counter2 >= 4 and counter2-counter1 == 1:
        return "Ventaja para P2"
    #Ahora vamos a hacer el return para los casos normales
    return puntos_a_terminos[counter1] + " - " + puntos_a_terminos[counter2]


if __name__ == "__main__":
    iteracion_secuencia(secuencia= secuencia_prueba)