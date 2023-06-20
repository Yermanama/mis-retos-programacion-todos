from diccionario import leet_dict

texto_introducido = input("Introduce el texto que quieras que sea traducido: \n")

def traduccion_normal_l33t(texto):
    traduccion = texto
    for letra, equivalente in leet_dict.items():
        traduccion = traduccion.replace(letra, equivalente)
    return traduccion

def traduccion_inversa(texto):
    traduccion = texto
    for letra, equivalente in leet_dict.items():
        traduccion = traduccion.replace(equivalente, letra)
    return traduccion

def decision_traductor(texto):
    letras_leet = set(leet_dict.values())
    if any(letra in letras_leet for letra in texto):
        return traduccion_inversa(texto)
    else:
        return traduccion_normal_l33t(texto)


if __name__ == "__main__":
    traduccion = decision_traductor(texto_introducido)
    print(traduccion)