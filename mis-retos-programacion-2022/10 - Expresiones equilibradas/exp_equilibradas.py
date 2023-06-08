"""Crea un programa que comprueba si los paréntesis, llaves y corchetes
de una expresión están equilibrados.
Equilibrado significa que estos delimitadores se abren y cieran
en orden y de forma correcta.
Paréntesis, llaves y corchetes son igual de prioritarios.
No hay uno más importante que otro.
Expresión balanceada: { [ a * ( c + d ) ] - 5 }
Expresión no balanceada: { a * ( c + d ) ] - 5 }"""

balanceada_expresion = "{ [ a * ( c + d ) ] - 5 }"
no_balanceada_expresion = "{ a * ( c + d ) ] - 5 }"


def esta_balanceada(expresion: str):
    pila = []
    delimitadores = {"(": ")", "{": "}", "[": "]"}
    for caracter in expresion:
        if caracter in delimitadores.keys():
            pila.append(caracter)
        elif caracter in delimitadores.values():
            if not pila or delimitadores[pila.pop()] != caracter:
                return False
    return True


if __name__ == "__main__":
    print(esta_balanceada(balanceada_expresion))
    print(esta_balanceada(no_balanceada_expresion))
