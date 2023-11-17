def imprimir_pregunta(pregunta):
    print("\n" + pregunta["pregunta"])
    for letra, respuesta in pregunta["respuestas"].items():
        print(f"{letra}: {respuesta[0]}")

def main():
    from preguntas import cuestionario  # Importa tu cuestionario desde tu módulo

    # 1. Crea un diccionario que registre la cantidad de respuestas por cada casa
    resultados = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}

    # 2. Crea un bucle que itere sobre todas las preguntas en tu lista de cuestionario
    for pregunta in cuestionario:
        # 3. Dentro de este bucle, imprime la pregunta y las opciones de respuesta
        imprimir_pregunta(pregunta)

        # 4. Recoge la entrada del usuario usando input(). Asegúrate de que la respuesta sea válida
        respuesta_valida = False
        while not respuesta_valida:
            respuesta = input("Seleccione una opción (A, B, C o D): ")
            if respuesta.upper() in pregunta["respuestas"].keys():
                respuesta_valida = True
            else:
                print("Por favor, introduce una opción válida.")

        # 5. Una vez que tengas una respuesta válida, mira en el diccionario de respuestas de la pregunta
        # para determinar qué casa se asocia con esa respuesta y añade 1 a esa casa en tu diccionario de resultados
        casa = pregunta["respuestas"][respuesta.upper()][1]
        resultados[casa] += 1

    # 6. Una vez que hayas hecho todas las preguntas, mira en tu diccionario de resultados
    # para determinar qué casa tiene la mayor cantidad de respuestas
    casa_seleccionada = max(resultados, key=resultados.get)

    print("¡Felicidades! Has sido seleccionado para la casa " + casa_seleccionada + "!")

if __name__ == "__main__":
    main()
