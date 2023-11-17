from collections import Counter


def son_anagrama(word1: str, word2: str) -> None:
    word1_list = [letter for letter in word1]
    word2_list = [letter for letter in word2]
    word1_dict = Counter(word1_list)
    word2_dict = Counter(word2_list)

    if word1 == word2:
        print("Las palabras no son anagramas porque son la misma palabra.")
    else:
        if word1_dict == word2_dict:
            print("Las dos palabras son anagramas, ya que sus diccionarios son iguales.")
        else:
            print("Las dos palabras no son anagramas, porque sus diccionarios son distintos.")


if __name__ == '__main__':

    print("Hola, este un programa que va a comprobar si dos palabras son anagramas entre ellas. ")
    input1: str = input('Escribe la primera palabra: ')
    input2: str = input('Escribe la segunda palabra: ')
    son_anagrama(input1, input2)
