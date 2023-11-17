"""
Escribe una función que calcule si un número dado es un número de Armstrong
(o también llamado narcisista).
Si no conoces qué es un número de Armstrong, debes buscar información 
al respecto.
"""

def es_amstrong(numero: int) -> bool:
    digitos_numero_str = [] 
    for digito in str(numero):
        digitos_numero_str.append(digito)
    suma = 0
    for digito in digitos_numero_str:
        suma += int(digito)**(len(list(digitos_numero_str)))
    if suma == numero:
        return True
    else:
        return False
    

print(es_amstrong(153))
print(es_amstrong(1234))
print(es_amstrong(370))
print(es_amstrong(2))