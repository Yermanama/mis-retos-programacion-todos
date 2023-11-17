"""
Crea una función que sume 2 números y retorne su resultado pasados
unos segundos.
- Recibirá por parámetros los 2 números a sumar y los segundos que
  debe tardar en finalizar su ejecución.
- Si el lenguaje lo soporta, deberá retornar el resultado de forma
  asíncrona, es decir, sin detener la ejecución del programa principal.
  Se podría ejecutar varias veces al mismo tiempo.
"""

import time


def parar_y_enviar(numero1: int, numero2: int, tiempo: int):
    suma = numero1 + numero2
    print(f"Vamos a esperar {tiempo} segundos antes de realizar la suma.")
    time.sleep(tiempo)
    return f"La suma es: {suma}"

print(parar_y_enviar(2,2,4))
