"""
Llamar a una API es una de las tareas más comunes en programación.
Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
Aquí tienes un listado de posibles APIs: 
https://github.com/public-apis/public-apis

"""

import requests

try:        
    response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
    response.raise_for_status()
except requests.exceptions.ConnectionError:
    print("Hubo un problema con la conexión.")

if response.status_code == 200:
    print("La conexión ha sido exitosa.")
    data = response.json()
    print(data.keys())
else:
    print(f"Hubo un error al llamar a la API: {response.status_code}")