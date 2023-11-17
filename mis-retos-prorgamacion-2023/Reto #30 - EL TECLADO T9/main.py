
diccionario_correspondencia = {0: " ",
                               1: "1", 11: "A", 111: "B", 1111: "C",
                               2: "2", 22: "D", 222: "E", 2222: "F",
                               3: "3", 33: "G", 333: "H", 3333: 'I',
                               4: "4", 44: "J", 444: "K", 4444: "L",
                               5: "5", 55: "M", 555: "N", 5555: "O",
                               6: "6", 66: "P", 666: "Q", 6666: "R",
                               7: "7", 77: "S", 777: "T", 7777: "U",
                               8: "8", 88: "V", 888: "W", 8888: "X",
                               9: "9", 99: "Y", 999: "Z", 9999: "Ñ"
                               }


def comprobar_cadena(cadena: str):
    cadena_por_guiones = cadena.split("-")
    lista_respuesta = []
    for elemento in cadena_por_guiones:
        if 4 >= len(elemento) > 0:
            primer_digito = elemento[0]
            for digito in elemento:
                if digito != primer_digito:
                    return f"En la cadena {elemento}, hay dígitos que son distintos, lo cual no está permitido."
                break
            traduction_elemento = diccionario_correspondencia[int(elemento)]
            lista_respuesta.append(traduction_elemento)
            respuesta_final = "".join(lista_respuesta)

        else:
            return (f"La cadena {elemento} tiene demasiados dígitos, el máximo número de pulsaciones es de 4, "
                    f"lo siento...")
    return respuesta_final


if __name__ == "__main__":
    print(comprobar_cadena("1-11-111-1111-55-66-77-88-99"))
    print(comprobar_cadena("333-5555-4444-11-0-55-7777-555-22-5555"))
