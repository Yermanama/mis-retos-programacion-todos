""" * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría 'odnum aloH'"""

palabra: str = 'German'

lista_palabra = []
lista_al_reves = []

for letra in palabra:
    lista_palabra.append(letra)

for letra in range(len(lista_palabra) - 1, -1, -1):
    lista_al_reves.append(lista_palabra[letra])

palabra_reversa = "".join(lista_al_reves)
print(palabra_reversa)
