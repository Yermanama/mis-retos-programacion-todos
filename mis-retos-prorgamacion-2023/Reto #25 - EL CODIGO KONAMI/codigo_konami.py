"""
Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido
correctamente desde el teclado. 
Si sucede esto, debe notificarse mostrando un mensaje en la terminal.

Código konami: ↑ ↑ ↓ ↓ ← → ← → B A
"""

import keyboard

inputs_lista = []

konami_lista = ['flecha arriba', 'flecha arriba', 'flecha abajo', 'flecha abajo', 'flecha izquierda', 'flecha derecha', 'flecha izquierda', 'flecha derecha', 'b', 'a']

def añadir_tecla(evento):
    if evento.name in konami_lista:
        inputs_lista.append(evento.name)
    else: 
        inputs_lista.clear()

keyboard.on_press(añadir_tecla)

while True:
    if len(inputs_lista) >= 10:
        if inputs_lista[-10:] == konami_lista:
            print('HAS ACTIVADO EL CÓDIGO KONAMI')
        inputs_lista.pop(0)


