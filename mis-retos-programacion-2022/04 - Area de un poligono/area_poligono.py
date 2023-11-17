""" * Crea una única función (importante que solo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro solo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""


def area_poligono(poligono: str, base, altura):
    if poligono.lower() == "triangulo":
        return (base * altura) / 2
    elif poligono.lower() == "cuadrado":
        return base * base
    elif poligono.lower() == "rectangulo":
        return base * altura
    else:
        print("Por favor, introduce el nombre de uno de los polígonos aceptados \n"
              "[Triangulo, Cuadrado, Rectangulo]")


if __name__ == "__main__":
    print("Este es un pequeño programa para calcular el área de uno de estos polígonos\n"
          "[Triangulo, Cuadrado, Rectangulo]")
    print(f'Triángulo {area_poligono("triangulo", 10, 5)}')
    print(f'Cuadrado {area_poligono("cuadrado", 5, 5)}')
    print(f'Rectangulo {area_poligono("rectangulo", 10,10)}')
