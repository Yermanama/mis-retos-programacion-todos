"""
Crea una función que reciba dos array, un booleano y retorne un array.
- Si el booleano es verdadero buscará y retornará los elementos comunes
  de los dos array.
- Si el booleano es falso buscará y retornará los elementos no comunes
  de los dos array.
- No se pueden utilizar operaciones del lenguaje que
  lo resuelvan directamente.
 """


def comparacion(lista1: list, lista2 : list, booleano: bool):
    if booleano:
        comunes_lista = []
        for elemento in lista1:
            if elemento in lista2:
                comunes_lista.append(elemento)
        return comunes_lista
    else:
        no_comunes_lista = []
        for elemento in lista1:
            if elemento not in lista2:
                no_comunes_lista.append(elemento)
        return no_comunes_lista
        

if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5, 6, 7]
    lista2 = [4, 5, 6, 7, 8, 9, 10]

    print(f'Elementos comunes en las dos listas: {comparacion(lista1=lista1, lista2=lista2, booleano=True)}')
    print(f'Elementos NO comunes en las dos listas: {comparacion(lista1=lista1, lista2=lista2, booleano=False)}')