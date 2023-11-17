letras_originales = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_codificadas = ""

for letra in letras_originales:
    if letra == "X":
        letras_codificadas += "A"
    elif letra == "Y":
        letras_codificadas += "B"
    elif letra == "Z":
        letras_codificadas += "C"
    else:
        letras_codificadas += chr(ord(letra) + 3)

normal_codificado_dict = {letras_originales[i]: letras_codificadas[i] for i in range(len(letras_originales))}

codificado_normal_dict = {valor: llave for llave, valor in normal_codificado_dict.items()}


if __name__ == "__main__":
    print(f'Diccionario directo: {normal_codificado_dict}')
    print(f'Diccionario invertido: {codificado_normal_dict}')