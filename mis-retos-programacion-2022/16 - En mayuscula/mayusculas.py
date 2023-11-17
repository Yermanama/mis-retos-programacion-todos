"""
Crea una función que reciba un String de cualquier tipo y se encargue de
poner en mayúscula la primera letra de cada palabra.
- No se pueden utilizar operaciones del lenguaje que
  lo resuelvan directamente.
"""
import string

minusculas = string.ascii_lowercase
mayusculas = string.ascii_uppercase

texto = "hola, este es un ejemplo de texto para probar la función"
diccionario = dict(zip(minusculas, mayusculas))

def convertir_a_mayusculas(texto: str) -> str:
    lista_palabras = texto.split(" ")
    mayusculas_lista = []
    for palabra in lista_palabras:
        lista_letras = [letra for letra in palabra]
        lista_letras[0] = diccionario[lista_letras[0]]
        palabra = "".join(lista_letras)
        mayusculas_lista.append(palabra)
    convertida = " ".join(mayusculas_lista)
    return convertida

print(convertir_a_mayusculas(texto))