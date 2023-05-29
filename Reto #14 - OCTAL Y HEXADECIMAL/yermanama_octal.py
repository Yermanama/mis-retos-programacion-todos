"""
Crea una función que reciba un número decimal y lo trasforme a Octal
y Hexadecimal.
- No está permitido usar funciones propias del lenguaje de programación que
realicen esas operaciones directamente.
"""

def decimal_octal(numero_decimal: int):
    numero_octal = []
    while  numero_decimal > 0: 
        resto = numero_decimal % 8
        numero_decimal = numero_decimal // 8
        numero_octal.append(resto)
    numero_octal = "".join(str(num) for num in reversed(numero_octal))
    return numero_octal

def decimal_hexal(numero_decimal: int):
    digitos_hexadecimales = "0123456789ABCDEF" 
    numero_hexadecimal = []
    while numero_decimal > 0:
        resto = numero_decimal % 16
        numero_hexadecimal.append(digitos_hexadecimales[resto])
        numero_decimal = numero_decimal // 16
    numero_hexadecimal = "".join(str(num) for num in reversed(numero_hexadecimal))
    return numero_hexadecimal


if __name__ == "__main__":
    print(decimal_octal(12))
    print(decimal_hexal(28))