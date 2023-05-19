"""
Escribe un programa que, dado un número, compruebe y muestre si es primo,
fibonacci y par.
Ejemplos:
- Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
- Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""

def comprobar_primo(numero):
    lista = []
    for n in range(1,numero):
        if numero % n == 0:
            lista.append(n)
    if len(lista) > 2:
        return "no es primo"
    else:
        return "es primo"

def comprobar_fibonacci(numero):
    a, b = 0, 1
    while a < numero:
        a, b = b, a+b
    if a == numero:
        return "fibonacci"
    else:
        return "no es fibonacci"

def comprobar_par(numero):
    if numero % 2 == 0:
        return "es par"
    else:
        return "es impar"

def imprimir_resultados():
    numero = input("Dime un número para comprobar si es par, fibonacci y primo\n")

    while not isinstance(numero, int):
        try:
            numero = int(numero)
        except ValueError:
            print("Esto no es un número válido. Intenta de nuevo")
            numero = input("Dime un número para comprobar si es par, fibonacci y primo\n")

    print(f"El número {numero} {comprobar_primo(numero)}, {comprobar_fibonacci(numero)} y {comprobar_par(numero)}.")


if __name__ == "__main__":
    imprimir_resultados()