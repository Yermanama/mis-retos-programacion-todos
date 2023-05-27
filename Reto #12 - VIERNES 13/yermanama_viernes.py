"""
Crea una función que sea capaz de detectar si existe un viernes 13
en el mes y el año indicados.
- La función recibirá el mes y el año y retornará verdadero o falso.
 """


from datetime import date

def es_viernes_13(año, mes):
    fecha = date(año, mes, 13)
    if fecha.weekday() == 4:
        return True
    else:
        return False
    

if __name__ == "__main__":
    print(es_viernes_13(2023, 1))