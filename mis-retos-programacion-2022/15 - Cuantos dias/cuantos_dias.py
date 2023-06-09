"""
Crea una función que calcule y retorne cuántos días hay entre dos cadenas
de texto que representen fechas.
- Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
- La función recibirá dos String y retornará un Int.
- La diferencia en días será absoluta (no importa el orden de las fechas).
- Si una de las dos cadenas de texto no representa una fecha correcta se
  lanzará una excepción.
"""

from datetime import datetime

def cuantos_dias(primera_cadena_fecha: str, segunda_cadena_fecha: str) -> int:
    try:
        primer_datetime = datetime.strptime(primera_cadena_fecha, "%d/%m/%Y")
        segundo_datetime = datetime.strptime(segunda_cadena_fecha, "%d/%m/%Y")
    except ValueError:
        raise ValueError("Una o ambas de las cadenas proporcionadas no es un formato válido para esta función.")
        
    primer_datetime = primer_datetime.date()
    segundo_datetime = segundo_datetime.date()
    diferencia = abs(primer_datetime.toordinal() - segundo_datetime.toordinal())
    return diferencia


    
print(cuantos_dias("12/05/2023", "27/11/2022"))
