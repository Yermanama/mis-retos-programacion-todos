"""
¿Sabías que puedes leer información de Git y GitHub desde la gran
mayoría de lenguajes de programación?
Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
- Hash
- Autor
- Mensaje
- Fecha y hora
Ejemplo de salida:
Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
Se permite utilizar librerías que nos faciliten esta tarea.
"""

import git
import os

ruta_de_trabajo = r"C:\Users\marti\OneDrive\Escritorio\CarpetaPrueba"
os.chdir(ruta_de_trabajo)
repo = git.Repo(ruta_de_trabajo)

commit_counter = 1 

for commit in list(repo.iter_commits())[:10]:
    print(f"Commit {commit_counter} | {commit.hexsha} | {commit.author.name} | {commit.message} | {commit.committed_date}")
    commit_counter += 1 
