"""
Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
resultado e imprímelo.
- El .txt se corresponde con las entradas de una calculadora.
- Cada línea tendrá un número o una operación representada por un
  símbolo (alternando ambos).
- Soporta números enteros y decimales.
- Soporta las operaciones suma "+", resta "-", multiplicación "*"
  y división "/".
- El resultado se muestra al finalizar la lectura de la última
  línea (si el .txt es correcto).
- Si el formato del .txt no es correcto, se indicará que no se han
  podido resolver las operaciones.
"""

with open(r"C:\Users\marti\OneDrive\Escritorio\Programación\mis-retos-programacion\mis-retos-programacion-2022\21 - Calculadora txt\enunciado.txt", 'r') as archivo:
    contenido_archivo = archivo.readlines()


def limpiar(x):
    return x.strip()


lista_de_input = list(map(limpiar, contenido_archivo))

print(lista_de_input)