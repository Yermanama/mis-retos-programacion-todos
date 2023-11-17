"""
Crea una función que reciba días, horas, minutos y segundos (como enteros)
y retorne su resultado en milisegundos.
"""

def convertir_milisegundos(dias: int, horas: int, minutos: int, segundos: int) -> int:
    dias_milisegundos = dias * 24 * 60 * 60 * 1000
    horas_milisegundos = horas * 60 * 60 * 1000
    minutos_milisegundos = minutos * 60 * 1000
    segundos_milisegundos = segundos * 1000
    milisegundos: int = dias_milisegundos + horas_milisegundos + minutos_milisegundos + segundos_milisegundos
    return f"Milisegundos : {milisegundos}"

print(convertir_milisegundos(12,12,12,12))