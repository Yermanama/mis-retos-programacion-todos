"""
Crea un programa que encuentre y muestre todos los pares de números primos
gemelos en un rango concreto.
El programa recibirá el rango máximo como número entero positivo.

- Un par de números primos se considera gemelo si la diferencia entre
  ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
- Ejemplo: Rango 14
  (3, 5), (5, 7), (11, 13)

"""

def obtener_primos_gemelos(top:int):
    lista_primos = []
    lista_gemelos = []
    for numero in range(1, top + 1, 1):
        divisibles = []
        for divisible in range(1, numero + 1, 1):
            if numero % divisible == 0:
                divisibles.append(divisible)
        if len(divisibles) == 2:
            lista_primos.append(numero)
    for primo in range(len(lista_primos)-1):
        if lista_primos[primo + 1] - lista_primos[primo] == 2:
            lista_gemelos.append((lista_primos[primo], lista_primos[primo + 1]))
    print(lista_gemelos)

if __name__ == "__main__":
    obtener_primos_gemelos(14)