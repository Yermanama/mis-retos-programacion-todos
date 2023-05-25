"""
Crea 3 funciones, cada una encargada de detectar si una cadena de
texto es un heterograma, un isograma o un pangrama.
- Debes buscar la definición de cada uno de estos términos.
"""
from string import ascii_lowercase

def heterograma(palabra: str):
    lista_letras = []
    for letra in palabra:
        if letra in lista_letras:
            print(f"{palabra} no es un heterograma, se repite la letra -> {letra}")
            break
        else:
            lista_letras.append(letra)

def isograma(palabra: str):
    diccionario_letras = {}
    for letra in palabra:
        if letra in diccionario_letras.keys():
            diccionario_letras[letra] += 1
        else:
            diccionario_letras[letra] = 1
    
    lista_letras = list(diccionario_letras.values())
    primer_valor = lista_letras[0]

    for letra, repeticiones in diccionario_letras.items():
        if repeticiones != primer_valor:
            print(f"No todas las letras de {palabra} se repiten el mismo número de veces. La letra -> {letra} se repite {repeticiones}, a diferencia de {primer_valor}")
        else:
            print(f"{palabra} es un isograma")
        
def pangrama(palabra: str):
    palabra = palabra.replace(" ", "")
    lista_palabra = set(sorted([letra for letra in palabra]))
    lista_abecedario = set([letra for letra in ascii_lowercase])

    print(lista_palabra)
    print(lista_abecedario)


if __name__ == "__main__":
    input_palabra = input("Dime la palabra que quieres que se compruebe: ")
    pangrama(input_palabra)