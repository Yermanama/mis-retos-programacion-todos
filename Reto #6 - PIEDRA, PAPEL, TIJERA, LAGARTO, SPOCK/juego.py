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
    eleccion = input("Escribe 5 elecciones para jugar:[piedra, papel, tijera, lagarto, spock]")
    lista_jugador = eleccion.split("")
    return lista_jugador

def obtener_pares():
    lista_elecciones_p1 = obtener_eleccion_jugador()
    lista_elecciones_p2 = obtener_eleccion_jugador()
    lista_tuplas = list(zip(lista_elecciones_p1, lista_elecciones_p2))
    return lista_tuplas

def obtener_marcador():
    pass