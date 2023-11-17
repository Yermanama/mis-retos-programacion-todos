"""* Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente."""


def decimal_binario(numero: int):
    cociente: int = numero
    lista_binario: list = []
    while cociente != 0:
        resto = cociente % 2
        lista_binario.append(resto)
        cociente = int(cociente/2)

    lista_binario_reversed = reversed(lista_binario)
    numero_binario = int("".join(map(str, lista_binario_reversed)))
    return numero_binario


if __name__ == "__main__":
    print(decimal_binario(5))
    print(decimal_binario(10))
    print(decimal_binario(22))
