import tkinter as tk
from tkinter import messagebox
from algorithm import get_knight_tour

# Configuración de la ventana y el tablero

BOARD_SIZE = 8
CELL_SIZE = 80

WIDTH = BOARD_SIZE * CELL_SIZE
HEIGHT = BOARD_SIZE * CELL_SIZE

MOVE_DELAY = 300

LIGHT_COLOR = "#F0D9B5"
DARK_COLOR = "#B58863"

# Crear ventana principal y canvas para dibujar el tablero y el caballo.

root = tk.Tk()
root.title("Recorrido del Caballo")

frame = tk.Frame(root)
frame.pack()

canvas = tk.Canvas(
    frame,
    width=WIDTH,
    height=HEIGHT
)
canvas.pack()

# Cargar la imagen del caballo.

try:
    knight_image = tk.PhotoImage(file="knight.png")
except Exception:
    messagebox.showerror(
        "Error",
        "No se encontró knight.png"
    )
    root.destroy()
    raise SystemExit

# Variables globales

selected_start = None
knight = None
path = []
current_step = 0

number_labels = []

path_lines = []

# Dibujar el tablero de ajedrez con colores alternados simulando un tablero real.

def draw_board():

    canvas.delete("square")

    for row in range(BOARD_SIZE):

        for col in range(BOARD_SIZE):

            color = (
                LIGHT_COLOR
                if (row + col) % 2 == 0
                else DARK_COLOR
            )

            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE

            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            canvas.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                fill=color,
                outline="black",
                tags="square"
            )

draw_board()

# Marcar la casilla seleccionada por el usuario como la posición inicial que tomara el 
# algoritmo para generar el recorrido del caballo.

start_marker = None

def select_square(event):

    global selected_start
    global start_marker

    col = event.x // CELL_SIZE
    row = event.y // CELL_SIZE

    selected_start = (col, row)

    if start_marker:
        canvas.delete(start_marker)

    x1 = col * CELL_SIZE
    y1 = row * CELL_SIZE

    x2 = x1 + CELL_SIZE
    y2 = y1 + CELL_SIZE

    start_marker = canvas.create_rectangle(
        x1,
        y1,
        x2,
        y2,
        outline="red",
        width=4
    )

canvas.bind("<Button-1>", select_square)

# Limpiar los números de movimiento del recorrido anterior antes de iniciar otra simulación.

def clear_numbers():

    for item in number_labels:
        canvas.delete(item)

    number_labels.clear()

# Crear el caballo en la posición inicial que ha sido seleccionada.

def create_knight(x, y):

    global knight

    px = x * CELL_SIZE + CELL_SIZE // 2
    py = y * CELL_SIZE + CELL_SIZE // 2

    knight = canvas.create_image(
        px,
        py,
        image=knight_image
    )

# Mostrar el número de movimiento en cada casilla a medida que el caballo avanza por el tablero.

def draw_move_number(x, y, move_number):

    px = x * CELL_SIZE + CELL_SIZE // 2
    py = y * CELL_SIZE + CELL_SIZE // 2

    text_id = canvas.create_text(
        px,
        py,
        text=str(move_number),
        font=("Arial", 12, "bold"),
        fill="#016681"
    )

    number_labels.append(text_id)
    
# Dibujar una línea entre cada movimiento del caballo para visualizar mejor el recorrido.
def draw_path_segment(x1, y1, x2, y2):

    px1 = x1 * CELL_SIZE + CELL_SIZE // 2
    py1 = y1 * CELL_SIZE + CELL_SIZE // 2

    px2 = x2 * CELL_SIZE + CELL_SIZE // 2
    py2 = y2 * CELL_SIZE + CELL_SIZE // 2

    line = canvas.create_line(
        px1,
        py1,
        px2,
        py2,
        width=3,
        fill="#be8dff",
        smooth=True
    )

    path_lines.append(line)

# Limpiar las líneas del recorrido anterior antes de iniciar otra simulación.
def clear_path():

    for line in path_lines:
        canvas.delete(line)

    path_lines.clear()

# Animación del recorrido del caballo para mover el caballo a cada posición
# del recorrido generado por el algoritmo.

def animate():

    global current_step

    if current_step >= len(path):
        return

    x, y = path[current_step]
    px = x * CELL_SIZE + CELL_SIZE // 2
    py = y * CELL_SIZE + CELL_SIZE // 2
    
    if current_step > 0:
        prev_x, prev_y = path[current_step - 1]

        draw_path_segment(
            prev_x,
            prev_y,
            x,
            y
        )
    
    if current_step < len(path) - 1:
        next_x, next_y = path[current_step + 1]
        
        preview = canvas.create_line(
            px,
            py,
            next_x * CELL_SIZE + CELL_SIZE // 2,
            next_y * CELL_SIZE + CELL_SIZE // 2,
            dash=(5, 5),
            width=2,
            fill="green"
        )

    canvas.coords(
        knight,
        px,
        py
    )

    draw_move_number(
        x,
        y,
        current_step + 1
    )

    current_step += 1

    root.after(
        MOVE_DELAY,
        animate
    )

# Iniciar recorrido al hacer click en el botón.

def start_simulation():

    global knight
    global path
    global current_step

    if selected_start is None:

        messagebox.showwarning(
            "Aviso",
            "Selecciona una casilla inicial"
        )

        return

    clear_numbers()
    clear_path()

    if knight:
        canvas.delete(knight)

    start_x, start_y = selected_start

    path = get_knight_tour(
        start_x,
        start_y
    )

    create_knight(
        start_x,
        start_y
    )

    current_step = 0

    animate()

# Crear botón para iniciar el recorrido.

button = tk.Button(
    root,
    text="Iniciar recorrido",
    command=start_simulation
)

button.pack(pady=10)

# Iniciar el bucle principal de la aplicación.
root.mainloop()