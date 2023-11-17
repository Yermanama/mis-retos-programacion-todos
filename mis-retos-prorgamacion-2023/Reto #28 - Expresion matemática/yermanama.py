def es_numero(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False


def es_expresion(expresion):
    operaciones_soportadas = ['+', '-', '*', '/', '%']
    return expresion in operaciones_soportadas


def comprobar_expresion(expresion: str) -> bool:
    nueva_expresion = expresion.split(' ')

    if len(nueva_expresion) % 2 == 0:
        print('No es una expresión válida puesto que una expresión debe de ser impar.')
        return False

    for item in range(len(nueva_expresion)):
        if item % 2 == 0:
            if not es_numero(nueva_expresion[item]):
                return False
        else:
            if not es_expresion(nueva_expresion[item]):
                return False
    return True


if __name__ == '__main__':
    print(comprobar_expresion('5 + 6 / 7 - 4'))
    print(comprobar_expresion('5 a 6'))
