"""
Crea una función que dibuje una escalera según su número de escalones.
- Si el número es positivo, será ascendente de izquiera a derecha.
- Si el número es negativo, será descendente de izquiera a derecha.
- Si el número es cero, se dibujarán dos guiones bajos (__).

Ejemplo: 4
        _
      _|       
    _|
  _|
_|

"""

def draw_ladders(steps:int):
    if steps == 0:
        print("__")
    elif steps > 0:
        for escalon in range(0, steps):
            espacios = " " * (steps - escalon)
            parte_pintada = "_" if escalon == 0 else "_|"
            print(f"{espacios}{parte_pintada}")
    else:
        for escalon in range(0, abs(steps)):
            espacios = " " * (escalon)
            parte_pintada = "_" if escalon == 0 else "|_"
            print(f"{espacios}{parte_pintada}")

if __name__ == "__main__":
    draw_ladders(0)
    draw_ladders(9)
    draw_ladders(-9)