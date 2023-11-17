from time import sleep


def cuenta_atras(primer_numero: int, segundos: int):
    if not isinstance(primer_numero, int) or not isinstance(segundos, int) or primer_numero < 0 or segundos < 0:
        print('Ingresa, por favor, numeros enteros positivos.')

    for numero in range(primer_numero, -1, -1):
        print(numero)
        sleep(segundos)


if __name__ == "__main__":
    cuenta_atras(5, 1)
    cuenta_atras(-2, 2)
