'''
Crea un programa que calcule quien gana más partidas al piedra,
papel, tijera.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La función recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "R" (piedra), "P" (papel)
  o "S" (tijera).
- Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
'''

entrada = [("R","S"), ("S","R"), ("P","S")]

posibles_respuestas = ('p', 'r', 's')

def asignar_ataques(entrada: list):
    primer_jugador_ataques = []
    segundo_jugador_ataques = []
    for combate in entrada:
        primer_jugador_ataques.append(combate[0])
        segundo_jugador_ataques.append(combate[1])
    return primer_jugador_ataques, segundo_jugador_ataques

primer_jugador_ataques, segundo_jugador_ataques = asignar_ataques(entrada=entrada)

def partida(primer_jugador: list, segundo_jugador: list):
    contador1 = 0
    contador2 = 0
    for ataque1, ataque2 in zip(primer_jugador, segundo_jugador):
            if ataque1 == ataque2:
                continue
            elif ataque1 == 'R' and ataque2 == 'S':
                contador1 += 1
            elif ataque1 == 'S' and ataque2 == 'P':
                contador1 += 1
            elif ataque1 == 'P' and ataque2 == 'R':
                contador1 += 1
            else:
                contador2 += 1
    return contador1, contador2

resultado1, resultado2 = partida(primer_jugador_ataques, segundo_jugador_ataques)

def determinar_ganador(resultado1, resultado2):
    if resultado1 == resultado2:
        return 'Tie'
    elif resultado1 > resultado2:
        return 'Ganador Jugador 1'
    else:
        return 'Ganador Jugador 2'
    
print(determinar_ganador(resultado1, resultado2))   