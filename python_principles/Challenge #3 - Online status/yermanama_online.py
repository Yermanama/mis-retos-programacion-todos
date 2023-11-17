statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(diccionario):
    contador = 0
    for persona in diccionario:
        if diccionario[persona] == "online":
            contador += 1
    return contador

print(online_count(statuses))
