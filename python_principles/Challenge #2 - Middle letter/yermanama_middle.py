"""Middle letter
Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return ""."""

def middle_letter(palabra):
    if len(palabra) %2 == 0:
        return ""
    else: 
        letra = palabra[int(len(palabra)/2)]
        return letra
    
print(middle_letter("abc"))

print(middle_letter("aaaa"))