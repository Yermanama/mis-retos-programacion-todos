"""
Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
- El juego comienza proponiendo una palabra aleatoria incompleta
  - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
- El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
  la palabra a adivinar)
  - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
    uno al número de intentos
  - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
    al número de intentos
  - Si el contador de intentos llega a 0, el jugador pierde
- La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
  ocultando más del 60%
- Puedes utilizar las palabras que quieras y el número de intentos que consideres
"""

from random import sample, randint, choice
from palabras import lista_palabras

numero_intentos = 5
palabra = random.choice(lista_palabras)
print(palabra)

lista_letras = [letra for letra in palabra]
numero_ocultos = randint(round(len(lista_letras)*0.6))
print(numero_ocultos)

for letra in lista_letras:
    if random.randint(0,1) == 1:
        posicion = lista_letras.index(letra)
        lista_letras[posicion] = "-"

print(lista_letras)