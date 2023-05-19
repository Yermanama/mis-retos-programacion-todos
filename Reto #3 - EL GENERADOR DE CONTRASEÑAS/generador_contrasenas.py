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


def obtener_entrada_usuario(prompt, opciones_validas):
    while True:
        entrada = input(prompt).lower()
        if entrada in opciones_validas:
            return entrada
        print(f"Entrada inválida. Opciones válidas son: {','.join(opciones_validas)}")


def generacion_contrasena():
    numero_caracteres = 0
    mayusculas = ""
    numeros = ""
    simbolos = ""

    numero_caracteres = obtener_entrada_usuario(
        "Dime un número entre el 8 y el 16, que va a ser la longtud de tu contraseña.",
        map(str, range(8, 16)),
    )
    numero_caracteres = int(numero_caracteres)

    mayusculas = obtener_entrada_usuario(
        "¿Quieres que se incluyan letras mayúsculas en tu contraseña?[Si/No]\n",
        ["si", "no"],
    )
    numeros = obtener_entrada_usuario(
        "¿Quieres que se incluyan números en tu contraseña?[Si/No]\n", ["si", "no"]
    )
    simbolos = obtener_entrada_usuario(
        "¿Quieres que se incluyan símbolos en tu contraseña?[Si/No]\n", ["si", "no"]
    )

    posibilidades = []
    posibilidades.extend(list(string.ascii_lowercase))
    if mayusculas == "si":
        posibilidades.extend(list(string.ascii_uppercase))
    if numeros == "si":
        posibilidades.extend(list(string.digits))
    if simbolos == "si":
        posibilidades.extend(list(string.punctuation))

    contrasena = random.choices(posibilidades, k=numero_caracteres)
    contrasena = "".join(contrasena)

    return contrasena


if __name__ == "__main__":
    print(f"Tu contraseña generada es: {generacion_contrasena()}")
