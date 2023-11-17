"""
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
La serie Fibonacci se compone por una sucesión de números en
la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""

primer_numero = 0
segundo_numero = 1
numero_imprimir = 0

 
for n in range(1, 51):
    print(numero_imprimir)
    numero_imprimir = segundo_numero
    segundo_numero += primer_numero
    primer_numero = numero_imprimir
