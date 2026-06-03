"""
Este archivo contiene únicamente la lógica del recorrido del caballo
utilizando la heurística de Warnsdorff.
"""

import random

N = 8


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y


cx = [1, 1, 2, 2, -1, -1, -2, -2]
cy = [2, -2, 1, -1, 2, -2, 1, -1]


def limits(x, y):
    return 0 <= x < N and 0 <= y < N


def isempty(board, x, y):
    return limits(x, y) and board[y * N + x] < 0


def get_degree(board, x, y):
    count = 0

    for i in range(8):
        if isempty(board, x + cx[i], y + cy[i]):
            count += 1

    return count


def next_move(board, cell):
    min_deg_idx = -1
    min_deg = N + 1

    start = random.randint(0, 1000) % N

    for count in range(N):
        i = (start + count) % N

        nx = cell.x + cx[i]
        ny = cell.y + cy[i]

        degree = get_degree(board, nx, ny)

        if isempty(board, nx, ny) and degree < min_deg:
            min_deg_idx = i
            min_deg = degree

    if min_deg_idx == -1:
        return None

    nx = cell.x + cx[min_deg_idx]
    ny = cell.y + cy[min_deg_idx]

    board[ny * N + nx] = board[cell.y * N + cell.x] + 1

    cell.x = nx
    cell.y = ny

    return cell


def neighbour(x, y, xx, yy):
    for i in range(N):
        if (x + cx[i] == xx) and (y + cy[i] == yy):
            return True

    return False


def generate_closed_tour(start_x=3, start_y=2):
    """
    Devuelve una lista con la secuencia de posiciones:

    [
        (x0, y0),
        (x1, y1),
        ...
        (x63, y63)
    ]

    o None si no encuentra una solución.
    """

    board = [-1] * (N * N)

    cell = Cell(start_x, start_y)

    board[cell.y * N + cell.x] = 1

    path = [(cell.x, cell.y)]

    for _ in range(N * N - 1):
        result = next_move(board, cell)

        if result is None:
            return None

        path.append((cell.x, cell.y))

    if not neighbour(cell.x, cell.y, start_x, start_y):
        return None

    return path


def get_knight_tour(start_x=0, start_y=0):
    # Sigue intentando hasta encontrar una solución válida.

    while True:
        path = generate_closed_tour(start_x, start_y)

        if path:
            return path