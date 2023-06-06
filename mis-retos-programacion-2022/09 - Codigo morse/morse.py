"""Crea un programa que sea capaz de transformar texto natural a código
morse y viceversa.
- Debe detectar automáticamente de qué tipo se trata y realizar
  la conversión.
- En morse se soporta raya "—", punto".", un espacio" " entre letras
  o símbolos y dos espacios entre palabras"  ".
- El alfabeto morse soportado será el mostrado en
  https://es.wikipedia.org/wiki/Código_morse."""

from diccionario import morse_normal_dict, normal_morse_dict
import re

mensaje: str = "HELLO WORLD"
morse_mensaje: str = "···· · ·—·· ·—·· ———  ·—— ——— ·—· ·—·· —··"


def morse_normal(aviso: str):
    lista_palabras_morse = aviso.split("  ")
    lista_palabras_traducidas = []
    for palabra in lista_palabras_morse:
        palabra_traducida_actual = ""
        letras = palabra.split(" ")
        for letra in letras:
            palabra_traducida_actual = palabra_traducida_actual + str(morse_normal_dict[letra])
        lista_palabras_traducidas.append(palabra_traducida_actual)
    mensaje_traducido = ' '.join(lista_palabras_traducidas)
    return mensaje_traducido


def normal_morse(aviso: str):
    lista_palabras_normal = aviso.split()
    lista_palabras_traducidas = []
    for palabra in lista_palabras_normal:
        palabra_traducida_actual = ""
        for letra in palabra:
            palabra_traducida_actual = palabra_traducida_actual + normal_morse_dict[letra]
        lista_palabras_traducidas.append(palabra_traducida_actual)
    mensaje_traducido = '  '.join(lista_palabras_traducidas)
    return mensaje_traducido


def seleccion_traduccion(aviso: str):
    encontrado = re.search("·", aviso)
    if encontrado:
        print(morse_normal(aviso))
    else:
        print(normal_morse(aviso))


if __name__ == '__main__':
    seleccion_traduccion(mensaje)
    seleccion_traduccion(morse_mensaje)
