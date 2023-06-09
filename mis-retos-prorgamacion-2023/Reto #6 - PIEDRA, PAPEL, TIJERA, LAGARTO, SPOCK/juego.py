"""
Crea un programa que calcule quien gana más partidas al piedra,
papel, tijera, lagarto, spock.
El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
La función recibe un listado que contiene pares, representando cada jugada.
El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
"✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
Debes buscar información sobre cómo se juega con estas 5 posibilidades.
Piedra aplasta a tijera (como en el juego original).
Piedra aplasta a lagarto.
Papel cubre piedra (como en el original).
Papel refuta a Spock.
Tijeras cortan papel (como en el original).
Tijeras decapitan lagarto.
Lagarto come papel.
Lagarto envenena a Spock.
Spock vaporiza piedra.
Spock destroza tijeras.
"""

reglas = {
    "spock":["piedra", "tijeras"],
    "lagarto":["papel", "spock"],
    "piedra":["lagarto","tijera"],
    "papel":["piedra", "spock"],
    "tijera":["papel", "lagarto"],
}

def obtener_eleccion_jugador():
    while True:
        eleccion = input("Escribe 5 elecciones para jugar:[piedra, papel, tijera, lagarto, spock]:\n")
        lista_jugador = eleccion.split(", ")
        if all(eleccion in reglas.keys() for eleccion in lista_jugador):
            return lista_jugador
        print("Las opciones que has proporcionado no son adecuadas")

def obtener_pares():
    lista_elecciones_p1 = obtener_eleccion_jugador()
    lista_elecciones_p2 = obtener_eleccion_jugador()
    lista_tuplas = list(zip(lista_elecciones_p1, lista_elecciones_p2))
    return lista_tuplas

def obtener_marcador(lista):
    counter1 = 0
    counter2 = 0
    for tupla in lista:
        if tupla[1] in reglas[tupla[0]]:
            print(f"{tupla[0]} VS {tupla[1]}")
            print(f"{tupla[0]} gana a {tupla[1]}")
            counter1 += 1
        else:
            print(f"{tupla[0]} VS {tupla[1]}")
            if tupla[1] == tupla[0]:
                print("Empate, nadie gana puntos")
            else:
                print(f"{tupla[0]} gana a {tupla[1]}")
                counter2 += 1
        print(f"El marcador actual es Jugador 1: {counter1} VS Jugador 2: {counter2}")
    if counter1 == counter2:
        print("Tenemos un empate")
    elif counter1 > counter2:
        print("El jugador 1 ha ganado la partida")
    else:
        print("El jugador 2 ha ganado la partida")


if __name__ == "__main__":
    obtener_marcador(obtener_pares())