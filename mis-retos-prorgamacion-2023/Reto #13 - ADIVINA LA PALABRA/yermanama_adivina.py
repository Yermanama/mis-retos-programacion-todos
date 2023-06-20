"""
Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
- El juego comienza proponiendo una palabra aleatoria incompleta
  - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
- El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
  la palabra a adivinar)
  - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
    uno al número de intentos
  - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
    al número de intentos
  - Si el contador de intentos llega a 0, el jugador pierde
- La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
  ocultando más del 60%
- Puedes utilizar las palabras que quieras y el número de intentos que consideres
"""

from random import sample, randint, choice
from palabras import lista_palabras

numero_intentos = 5
lista_intentos = []

#Primero vamos a seleccionar una palabra aleatoria dentro de nuestra lista de palabras
palabra = choice(lista_palabras)

#Creamos una lista con las letras de la palabra y calculamos el número de letras que podemos ocultar para que nos se haga muy difícil
lista_letra = [letra for letra in palabra]
numero_ocultas = randint(1, round(len(lista_letra)*0.6))

#Ahora vamos a sustituir las letras por guiones en el caso de que queramos ocultarla
for indice in sample(range(len(lista_letra)), numero_ocultas):
    lista_letra[indice] = "-"

#Convertimos la lista en una cadena para mostrarselo al usuario de una manera más visual
palabra_oculta = "".join(lista_letra)
print(f"Palabra a adivinar: {palabra_oculta}")

#Ahora aquí vamos a aplicar la lógica del juego
while numero_intentos > 0 and "-" in palabra_oculta:
    print(f"Has probado ya con estas letras {lista_intentos}")
    intento = input("Adivina una letra o la palabra completa: ").lower().strip()
    if "-" not in palabra_oculta:
        print("¡Felicidades, has adivinado la palabra!")
        break
    if numero_intentos == 0:
        print(f"Lo siento, has agotado tus intentos. La palabra era {palabra}.")
    if len(intento) == 1:
        print(f"Has seleccionado la letra {intento}")
        lista_temporal = list(palabra_oculta)
        if intento in palabra:
            for i, letra in enumerate(palabra):
                if letra == intento: 
                    lista_temporal[i] = intento
                palabra_oculta = "".join(lista_temporal)
            print(f"La letra {intento} está en la palabra")
            print(f"El estado actual de la palabra a adivinar es: {palabra_oculta}")
        else:
            numero_intentos -= 1
            print(f"La letra {intento} no está en la palabra")
            lista_intentos.append(intento)
    elif len(intento) == len(palabra_oculta):
        print(f"Has seleccionado la palabra {intento}")
        if intento == palabra:
            print("¡Has ganado, enhorabuena!")
            palabra_oculta = palabra
            print(f"La palabra oculta era {palabra}")
        else:
            numero_intentos -= 1
            print(f"Has fallado, la palabra oculta no es {intento}.")
            print(f"Te quedan {numero_intentos} intentos.")
    else: 
        print("Por favor, introduce una letra o una palabra del mismo tamaño que la palabra a adivinar.")

