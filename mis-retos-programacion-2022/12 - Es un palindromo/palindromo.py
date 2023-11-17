"""
Escribe una función que reciba un texto y retorne verdadero o
falso (Boolean) según sean o no palíndromos.
Un Palíndromo es una palabra o expresión que es igual si se lee
de izquierda a derecha que de derecha a izquierda.
NO se tienen en cuenta los espacios, signos de puntuación y tildes.
Ejemplo: Ana lleva al oso la avellana.
"""
import string

def es_palindromo(palabra: str):
    tabla_traduccion = str.maketrans("", "", string.punctuation)
    palabra = palabra.translate(tabla_traduccion)
    palabra = palabra.replace(" ", "")
    palabra_inversa = "".join(reversed(list(palabra.lower())))
    print(f"La palabra al revés es : {palabra_inversa}")
    if palabra_inversa == palabra.lower():
        print("La palabra es un palíndromo, son iguales escritos normal y al revés.")


if __name__ == "__main__":
    es_palindromo("Ana lleva al oso la avellana.")