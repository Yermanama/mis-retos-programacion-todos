for numero in range(1, 101):
    lista_divisibles = []
    for n in range(1, numero + 1):
        if numero % n == 0:
            lista_divisibles.append(n)
    if len(lista_divisibles) == 2:
        print(numero)
