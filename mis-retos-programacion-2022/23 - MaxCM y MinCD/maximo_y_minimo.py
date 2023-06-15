"""
Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
que calcule el mínimo común múltiplo (mcm) de dos números enteros.
- No se pueden utilizar operaciones del lenguaje que 
  lo resuelvan directamente.
"""

def maximo_comun_divisor(numero1 :int, numero2: int) -> int:
    mcd = 1
    for numero in range(1, min(numero1, numero2)+ 1): # por cada número entre 1 y el menor de los dos números
        if numero1 % numero == 0 and numero2 % numero == 0: # si el resto de la división de los dos números entre dicho número es 0
            mcd = numero
    return mcd

def minimo_comun_multiplo(numero1: int, numero2: int) -> int:
    for numero in range(max(numero1, numero2), numero1 * numero2 + 1):
        if numero % numero1 == 0 and numero % numero2 == 0: 
            return numero
    return numero1 * numero2


if __name__ == "__main__":
    print(maximo_comun_divisor(12, 6))
    print(minimo_comun_multiplo(12, 6))
