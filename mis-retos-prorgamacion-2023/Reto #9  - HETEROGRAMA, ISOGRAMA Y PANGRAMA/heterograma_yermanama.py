"""
Crea 3 funciones, cada una encargada de detectar si una cadena de
texto es un heterograma, un isograma o un pangrama.
- Debes buscar la definición de cada uno de estos términos.
"""
from string import ascii_lowercase
from string import punctuation

def heterograma(palabra: str):
    palabra = palabra.lower()
    lista_letras = []
    for letra in palabra:
        if letra in lista_letras:
            print(f"{palabra} no es un heterograma, se repite la letra -> {letra}") 
            return False
        else:
            lista_letras.append(letra)
    return True

def isograma(palabra: str):
    palabra = palabra.lower()
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
            return False
        else:
            print(f"{palabra} es un isograma")
            return True
        
def pangrama(palabra: str): #Eliminar simbolos de puntuacion 
    palabra = palabra.lower()
    palabra_sin_espacios = palabra.replace(" ", "")
    palabra_sin_puntuacion = palabra_sin_espacios.replace(punctuation, "")
    lista_palabra = set(sorted([letra for letra in palabra_sin_puntuacion]))
    lista_abecedario = set([letra for letra in ascii_lowercase])

    if lista_abecedario.issubset(lista_palabra) == True:
        print(f"La frase/palabra {palabra} es un pangrama.")
        return True
    else: 
        print(f"La frase/palabra {palabra} es un pangrama.")
        return False


if __name__ == "__main__":
    input_palabra = input("Dime la palabra que quieres que se compruebe: ")
    diccionario_opciones = {"1":heterograma, "2":isograma, "3": pangrama}
    while True:
        print("1. Comprobar si la palabra es un heterograma.")
        print("2. Comprobar si la palabra es un isograma.")
        print("3. Comprobar si la palabra/frase es un paragrama.")
        print("4. Salir")
        opcion = input("Por favor, selecciona una opción:")
        if opcion in diccionario_opciones:
            comprobacion = diccionario_opciones[opcion](input_palabra)
            print(comprobacion)
        elif opcion == "4":
            break
        else:
            print("Opción no válida, inserte un número que corresponda con una de las cuatro opciones")
    