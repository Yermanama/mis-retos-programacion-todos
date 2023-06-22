import tkinter as tk
from tkinter import messagebox

class Conecta4:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Conecta 4")
        self.botones = [[tk.Button(self.window, width=10, height=3) for _ in range(6)] for _ in range(7)]
        for i in range(7):
            for j in range(6):
                self.botones[i][j].grid(row=j, column=i)
                self.botones[i][j].config(command= lambda row=i, col=j: self.hacer_movimiento(row, col))
        self.turno_rojo = True
        self.tablero = [['' for _ in range(6)] for _ in range(7)]
        self.label_turno = tk.Label(self.window, text="Turno: Rojo")
        self.label_turno.grid(row=7, column=0, columnspan=7)
        self.window.mainloop()

    
    def hacer_movimiento(self, row, col):
        for i in range(5, -1, -1):
            if self.tablero[row][i] == "":
                self.tablero[row][i] = 'R' if self.turno_rojo else 'A'
                self.botones[row][i].config(bg = 'red' if self.turno_rojo else 'yellow')

                self.turno_rojo = not self.turno_rojo
                self.label_turno.config(text = 'Turno: ' + ('Rojo' if self.turno_rojo else 'Amarillo'))
                if self.comprobar_victoria():
                    tk.messagebox.showinfo('Conecta 4', 'Ha ganado el jugador ' + ("Rojo" if not self.turno_rojo else "Amarillo"))
                break
    
    def comprobar_victoria(self):
        for col in range(7):  # recorremos las columnas
            for row in range(6):  # recorremos las celdas de cada columna
                if col <= 3:  # hay espacio para una línea de 4 celdas hacia la derecha
                    if self.tablero[col][row] != "" and \
                    self.tablero[col][row] == self.tablero[col+1][row] == self.tablero[col+2][row] == self.tablero[col+3][row]:
                        return True  # hay una línea de 4 celdas del mismo color
                if row <= 2:  # hay espacio para una línea de 4 celdas hacia abajo
                    if self.tablero[col][row] != "" and \
                    self.tablero[col][row] == self.tablero[col][row+1] == self.tablero[col][row+2] == self.tablero[col][row+3]:
                        return True  # hay una línea de 4 celdas del mismo color
                if col <= 3 and row <= 2:  # hay espacio para una línea de 4 celdas en diagonal abajo/derecha
                    if self.tablero[col][row] != "" and \
                    self.tablero[col][row] == self.tablero[col+1][row+1] == self.tablero[col+2][row+2] == self.tablero[col+3][row+3]:
                        return True  # hay una línea de 4 celdas del mismo color
                if col >= 3 and row <= 2:  # hay espacio para una línea de 4 celdas en diagonal abajo/izquierda
                    if self.tablero[col][row] != "" and \
                    self.tablero[col][row] == self.tablero[col-1][row+1] == self.tablero[col-2][row+2] == self.tablero[col-3][row+3]:
                        return True  # hay una línea de 4 celdas del mismo color
        return False  # no hay ninguna línea de 4 celdas del mismo color


        

if __name__ == "__main__":
    Conecta4()
