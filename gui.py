import os
import tkinter as tk

# Configuración de la ventana
BOARD_SIZE = 8
CELL_SIZE = 80

WINDOW_SIZE = BOARD_SIZE * CELL_SIZE

# VENTANA
root = tk.Tk()
root.title("Recorrido del Caballo")

canvas = tk.Canvas(
    root,
    width=WINDOW_SIZE,
    height=WINDOW_SIZE
)

canvas.pack()

root.mainloop()