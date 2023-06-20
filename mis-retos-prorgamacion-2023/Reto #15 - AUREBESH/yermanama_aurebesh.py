"""
Crea una función que sea capaz de transformar Español al lenguaje básico 
del universo Star Wars: el "Aurebesh".
- Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
- También tiene que ser capaz de traducir en sentido contrario.
 
¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
¡Que la fuerza os acompañe!
"""

from diccionario import aur_dict

def español_aurebesh(text: str, reverse = False):
    if reverse == True:
        for key, value in aur_dict.items():
            text = text.replace(value, key)
        return text
    else: 
        resul = ""
        contador = 0 
        while contador < len(text):
            char = ""
            char_seq = ""
            char = text[contador].lower()
            if (contador + 1) < len(text):
                char_seq = (text[contador] + text[contador + 1].lower())
            if char_seq in aur_dict:
                resul += aur_dict[char_seq]
                contador += 1
            else:
                if ( not char.isspace()) and ( char in aur_dict):
                    resul += aur_dict[char]
                elif char.isspace():
                    resul += " "
                else:
                    resul += char
        contador +=1
    return resul



if __name__ == "__main__":
    español_aurebesh("hola")