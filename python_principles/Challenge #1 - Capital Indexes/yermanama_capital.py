"""Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4]"""

def capital_indexes(palabra:str): 
    lista_mayusculas = []
    for posicion, letra in enumerate(palabra):
        if letra == letra.upper():
            lista_mayusculas.append(posicion)
    return lista_mayusculas

if __name__ == "__main__":
    print(capital_indexes("HeLlO"))