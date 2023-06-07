"""Crea un programa que comprueba si los paréntesis, llaves y corchetes
de una expresión están equilibrados.
Equilibrado significa que estos delimitadores se abren y cieran
en orden y de forma correcta.
Paréntesis, llaves y corchetes son igual de prioritarios.
No hay uno más importante que otro.
Expresión balanceada: { [ a * ( c + d ) ] - 5 }
Expresión no balanceada: { a * ( c + d ) ] - 5 }"""


import re

caracter_apertura = ["{", "[", "("]
caracter_cierre = ["}", "]", ")"]

balanceada_expresion = "{ [ a * ( c + d ) ] - 5 }"
no_balanceada_expresion = "{ a * ( c + d ) ] - 5 }"

pila = []

for caracter in no_balanceada_expresion:
    if caracter in caracter_apertura:
        pila.append(caracter)
    if caracter in caracter_cierre:
        if len(pila) == 0:
            print("La expresión no está balanceada porque tiene un caracter de cierre antes de uno de apertura.")
        if len(pila) != 0:
            ultimo_caracter = pila.pop()
            if 