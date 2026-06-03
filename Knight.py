"""
Problema: Un caballo se coloca en el primer bloque de un tablero vacío 
y moviéndose según las reglas del ajedrez, 
debe visitar cada casilla exactamente una vez. 
"""
import random

# Clase simple para almacenar las coordenadas (x, y) del caballo en el tablero
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
N = 8  # Tamaño del tablero (8x8)

# Estos arrays definen los 8 movimientos posibles de un caballo en ajedrez.
# Cada índice contiene cuántas posiciones se mueve en x e y respectivamente.
# Por ejemplo: cx[0]=1, cy[0]=2 significa "1 a la derecha, 2 hacia arriba"
cx = [1, 1, 2, 2, -1, -1, -2, -2]  # Cambios en coordenada X
cy = [2, -2, 1, -1, 2, -2, 1, -1]  # Cambios en coordenada Y

# Valida que las coordenadas (x, y) estén dentro del tablero de 8x8
# Retorna True si está dentro, False si está fuera
def limits(x, y):
    return ((x >= 0 and y >= 0) and (x < N and y < N))

# Comprueba si una casilla es válida para visitar:
# - Debe estar dentro del tablero (limits)
# - Debe estar vacía (no visitada, representado por valor < 0)
def isempty(a, x, y):
    return (limits(x, y)) and (a[y * N + x] < 0)

# Cuenta cuántas casillas vacías y válidas hay alrededor de la posición (x, y)
# Esto es clave en el algoritmo de Warnsdorff: se prefieren casillas con menos opciones
def getDegree(a, x, y):
    count = 0
    # Prueba los 8 posibles movimientos del caballo
    for i in range(N):
        if isempty(a, (x + cx[i]), (y + cy[i])):
            count += 1
    return count

# FUNCIÓN PRINCIPAL DEL ALGORITMO DE WARNSDORFF
# Heurística: El caballo siempre se mueve a la casilla vacía que tiene menos opciones futuras.
# Esto reduce la probabilidad de quedarse atrapado.
# Retorna el objeto Cell con la nueva posición, o None si no hay movimiento válido
def nextMove(a, cell):
    min_deg_idx = -1  # Índice del movimiento con grado mínimo (-1 significa "no encontrado")
    c = 0  # Contador temporal
    min_deg = (N + 1)  # Inicializa con un valor mayor que el máximo posible (8)
    nx = 0  # Nueva coordenada X
    ny = 0  # Nueva coordenada Y
    
    # Comienza desde un índice aleatorio para evitar patrones predecibles
    start = random.randint(0, 1000) % N
    
    # Prueba todos los 8 posibles movimientos del caballo
    for count in range(0, N):
        i = (start + count) % N  # Rota a través de los 8 movimientos
        nx = cell.x + cx[i]  # Calcula nueva X
        ny = cell.y + cy[i]  # Calcula nueva Y
        c = getDegree(a, nx, ny)  # Cuenta opciones futuras en esa casilla
        
        # Si la casilla es válida Y tiene menos opciones que el mínimo anterior,
        # la guardamos como la mejor opción
        if ((isempty(a, nx, ny)) and c < min_deg):
            min_deg_idx = i
            min_deg = c
    
    # Si no encontramos ningún movimiento válido, retorna None
    if (min_deg_idx == -1):
        return None
    
    # Calcula las coordenadas finales del movimiento
    nx = cell.x + cx[min_deg_idx]
    ny = cell.y + cy[min_deg_idx]
    
    # Marca esta casilla con el número de orden del movimiento
    # (suma 1 al número anterior para llevar el conteo)
    a[ny * N + nx] = a[(cell.y) * N + (cell.x)] + 1
    
    # Actualiza la posición actual del caballo
    cell.x = nx
    cell.y = ny
    
    return cell

# Imprime el tablero completo con todos los números de movimiento
# Muestra la secuencia en que se visitó cada casilla (1 a 64)
def printA(a):
    for i in range(N):
        for j in range(N):
            print("%d\t" % a[j * N + i], end="")
        print()

# Comprueba si la casilla final (xx, yy) es vecina de la casilla inicial (x, y)
# Esto verifica si el tour es "cerrado" (puede volver al inicio)
def neighbour(x, y, xx, yy):
    # Itera sobre los 8 posibles movimientos
    for i in range(N):
        # Si la nueva posición coincide con un movimiento válido desde (x, y), son vecinas
        if ((x + cx[i]) == xx) and ((y + cy[i]) == yy):
            return True
    return False

# FUNCIÓN PRINCIPAL: Ejecuta el algoritmo completo de Warnsdorff
# Retorna True si encuentra un tour cerrado válido, False si no
def findClosedTour():
    # Inicializa el tablero: -1 significa "no visitado"
    a = [-1] * N * N
    
    # Posición de inicio (casilla 3,2)
    sx = 3
    sy = 2
    
    # Crea un objeto Cell con la posición inicial
    cell = Cell(sx, sy)
    
    # Marca la casilla inicial como visitada con número 1
    a[cell.y * N + cell.x] = 1
    
    # Realiza N*N-1 movimientos (ya que la primera casilla cuenta como 1)
    # Intenta encontrar una secuencia válida de 64 casillas en un tablero 8x8
    ret = None
    for i in range(N * N - 1):
        ret = nextMove(a, cell)
        # Si nextMove retorna None, no hay movimiento válido: falla
        if ret == None:
            return False
    
    # Después de completar todos los movimientos, verifica si el tour es cerrado
    # Es decir: ¿el último movimiento puede conectar con el inicial?
    if not neighbour(ret.x, ret.y, sx, sy):
        return False
    
    # Si todo es válido, muestra el tablero y retorna éxito
    printA(a)
    return True

# Código ejecutable: Intenta resolver el problema hasta encontrar una solución
if __name__ == '__main__':
    # Ejecuta findClosedTour() una y otra vez hasta que retorne True
    # Esto es necesario porque el algoritmo es aleatorio y no siempre encuentra solución
    while not findClosedTour():
        pass