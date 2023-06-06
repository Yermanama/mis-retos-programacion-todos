""" * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
lo resuelvan automáticamente."""

import re

texto = "El viaje de la vida está lleno de desafíos, pero también de oportunidades. Cada día es una página en blanco" \
        " en la que podemos escribir nuestra historia. Aprovechemos cada momento para crecer, aprender y alcanzar" \
        " nuestros sueños. No importa cuán difícil sea el camino, siempre podemos encontrar la fuerza para seguir" \
        " adelante. ¡Nunca dejemos de soñar y perseguir aquello que nos hace felices!"

texto_minuscula = texto.lower()
lista_texto = re.split("\W+", texto_minuscula)
diccionario_texto = dict()
for palabra in lista_texto:
    if palabra not in diccionario_texto:
        diccionario_texto[palabra] = 1
    else:
        diccionario_texto[palabra] += 1

palabra_mas_repetida = max(diccionario_texto)
print(palabra_mas_repetida)
