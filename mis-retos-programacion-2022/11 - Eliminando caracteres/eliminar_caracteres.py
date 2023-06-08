"""
Crea una función que reciba dos cadenas como parámetro (str1, str2)
e imprima otras dos cadenas como salida (out1, out2).
out1 contendrá todos los caracteres presentes en la str1 pero NO
estén presentes en str2.
out2 contendrá todos los caracteres presentes en la str2 pero NO
estén presentes en str1.
"""


def diferencia_cadenas(cadena1: str, cadena2: str):
    lista1 = list(cadena1.lower())
    lista2 = list(cadena2.lower())
    out1 = []
    for caracter in lista1:
        if caracter not in lista2:
            out1.append(caracter)
    out2 = []
    for caracter2 in lista2:
        if caracter2 not in lista1:
            out2.append(caracter2)
    out1 = "".join(out1)
    out2 = "".join(out2)
    print(f"Los caracteres que están en la primera cadena y que no están en la segunda son los siguientes: "
          f"({out1})")
    print(f"Los caracteres que están en la segunda cadena y que no están en la primera son los siguientes: "
          f"({out2})")


if __name__ == "__main__":
    diferencia_cadenas(cadena1="Crea una función que reciba dos cadenas como parámetro",
                       cadena2="e imprima otras dos cadenas como salida")
