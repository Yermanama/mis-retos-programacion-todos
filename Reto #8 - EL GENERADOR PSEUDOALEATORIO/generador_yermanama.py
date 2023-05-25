"""
Crea un generador de números pseudoaleatorios entre 0 y 100.
- No puedes usar ninguna función "random" (o semejante) del 
  lenguaje de programación seleccionado.
Es más complicado de lo que parece...
 """

import time

def generar_numero_aleatorio():
    tiempo_minisegundos = time.time()
    tiempo_en_rango = (tiempo_minisegundos/10000000)%101
    return tiempo_en_rango

if __name__ == "__main__":
    numero_aleatorio = generar_numero_aleatorio()
    print(numero_aleatorio)