"""Escribe una función que calcule y retorne el factorial de un número dado
de forma recursiva."""

def factorial(numero: int):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

if __name__ == "__main__":
    print(factorial(5))
    print(factorial(10))