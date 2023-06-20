from texto import texto_ejemplo
import nltk
nltk.download("punkt")
from nltk.tokenize import sent_tokenize, word_tokenize 

def analizar_texto(texto):
    
    numero_palabras = len(word_tokenize(texto))
    numero_oraciones = len(sent_tokenize(texto))

    print(f"El número de palabras en el texto es de: {numero_palabras}")
    print(f"El número de oraciones en el texto es de: {numero_oraciones}")

    longitud_palabra_mas_larga = 0
    palabra_larga = ""
    longitud_total = 0

    for palabra in word_tokenize(texto):
        longitud_total += len(palabra)
        if len(palabra) > longitud_palabra_mas_larga: 
            longitud_palabra_mas_larga = len(palabra)
            palabra_larga = palabra 
    
    longitud_media = longitud_total / numero_palabras

    
    print(f"La palabra más larga del texto es: {palabra_larga}, que tiene {longitud_palabra_mas_larga}")
    print(f"La longitud media de las palabras del texto es de {longitud_media}")

if __name__ == "__main__":
    analizar_texto(texto_ejemplo)