"""
Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:
- Longitud: Entre 8 y 16.
- Con o sin letras mayúsculas.
- Con o sin números.
- Con o sin símbolos.
(Pudiendo combinar todos estos parámetros entre ellos)
"""
import random
import string


def generacion_contrasena():
    numero_caracteres = 0
    mayusculas = ""
    numeros = ""
    simbolos = ""

    while numero_caracteres not in list(range(8,16)):
        numero_caracteres = int(
            input("Dime un número del 8-16 para saber la longitud de tu contraseña.\n")
        )

    while mayusculas != "no" and mayusculas != "si":
        mayusculas = input(
            "¿Quieres que se incluyan letras mayúsculas en tu contraseña?[Si/No]\n"
        ).lower()

    while numeros != "no" and numeros != "si":
        numeros = input("¿Quieres que se incluyan números en tu contraseña?[Si/No]\n").lower()

    while simbolos != "no" and simbolos != "si":
        simbolos = input("¿Quieres que se incluyan números en tu contraseña?[Si/No]\n").lower()

    posibilidades = []
    posibilidades.append(list(string.ascii_lowercase))
    if mayusculas.lower() == "si":
        posibilidades.extend(list(string.ascii_uppercase))
    if numeros.lower() == "si":
        posibilidades.extend(list(string.digits))
    if simbolos.lower() == "si":
        posibilidades.extend(list(string.punctuation))

    contrasena = random.choices(posibilidades, k=numero_caracteres)
    contrasena = "".join(contrasena)

    return contrasena

if __name__ ==  "__main__":
    print(f"Tu contraseña generada es: {generacion_contrasena()}")