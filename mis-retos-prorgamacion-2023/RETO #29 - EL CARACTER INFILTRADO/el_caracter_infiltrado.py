'''
/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */
'''

def rabi(cadena_texto1: str, cadena_texto2: str):
    lista_primera = list(cadena_texto1)
    lista_segunda = list(cadena_texto2)
    lista_resultados = []
    for indice, letra in enumerate(lista_primera):
        if lista_primera[indice] != lista_segunda[indice]:
            lista_resultados.append(letra)
    print(lista_resultados)

rabi('Hola que tal', 'Hele que tol')