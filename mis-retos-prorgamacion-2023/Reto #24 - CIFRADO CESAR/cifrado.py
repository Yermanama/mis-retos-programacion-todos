"""
Crea un programa que realize el cifrado César de un texto y lo imprima.
También debe ser capaz de descifrarlo cuando así se lo indiquemos.
Te recomiendo que busques información para conocer en profundidad cómo
realizar el cifrado. Esto también forma parte del reto.
"""

from diccionario import normal_codificado_dict, codificado_normal_dict

def cifrar_texto(texto: str) -> str:
    texto_cifrado = ""
    for letra in texto:
        texto_cifrado += normal_codificado_dict[letra]
    return texto_cifrado

def descifrar_texto(texto: str) -> str:
    texto_descifrado = ""
    for letra in texto:
        texto_descifrado += codificado_normal_dict[letra]
    return texto_descifrado

def selector_cifrado(texto: str) -> str:
    posibilidades: list = ["C", "D"]
    eleccion = ""
    print(f"Tu texto es ({texto}), ¿qué quieres hacer con él?")
    while eleccion not in posibilidades:
        eleccion: str = input("Elige si quieres de CODIFICAR (C) o DESCODIFICAR (D): ")
    if eleccion == "C":
        resultado = cifrar_texto(texto.upper())
    else:
        resultado = descifrar_texto(texto.upper())
    
    return resultado.lower()


if __name__ == "__main__":
    ejemplo1 = "hola"
    ejemplo2 = "krod"
    print(f"El texto resultado es: {selector_cifrado(ejemplo1)}")
    print(f"El texto resultado es: {selector_cifrado(ejemplo2)}")
