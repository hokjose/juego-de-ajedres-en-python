# Representación de un ajedrez en consola

# Definición de piezas usando letras (mayúsculas = blancas, minúsculas = negras)
# P = Peón, R = Torre, N = Caballo, B = Alfil, Q = Reina, K = Rey

tablero = [
    ["r","n","b","q","k","b","n","r"],
    ["p","p","p","p","p","p","p","p"],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    ["P","P","P","P","P","P","P","P"],
    ["R","N","B","Q","K","B","N","R"]
]

turno = "blancas"  # Comienza el jugador blanco


def mostrar_tablero():
    print("   a b c d e f g h")
    for i, fila in enumerate(tablero):
        print(str(8-i) + " ", " ".join(fila), str(8-i))
    print("   a b c d e f g h\n")


def es_movimiento_valido(pieza, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    # Peón blanco
    if pieza == "P":
        if dx == -1 and dy == 0 and tablero[x2][y2] == ".":
            return True
        if dx == -2 and dy == 0 and x1 == 6 and tablero[x2][y2] == ".":
            return True
        if dx == -1 and abs(dy) == 1 and tablero[x2][y2].islower():
            return True
        return False

    # Peón negro
    if pieza == "p":
        if dx == 1 and dy == 0 and tablero[x2][y2] == ".":
            return True
        if dx == 2 and dy == 0 and x1 == 1 and tablero[x2][y2] == ".":
            return True
        if dx == 1 and abs(dy) == 1 and tablero[x2][y2].isupper():
            return True
        return False

    # Torre
    if pieza.lower() == "r":
        return dx == 0 or dy == 0

    # Alfil
    if pieza.lower() == "b":
        return abs(dx) == abs(dy)

    # Reina
    if pieza.lower() == "q":
        return dx == 0 or dy == 0 or abs(dx) == abs(dy)

    # Rey
    if pieza.lower() == "k":
        return abs(dx) <= 1 and abs(dy) <= 1

    # Caballo
    if pieza.lower() == "n":
        return (abs(dx), abs(dy)) in [(2,1),(1,2)]

    return False


def mover_pieza(origen, destino):
    global turno

    # Convertir de notación ajedrecística a índices de lista
    columnas = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
    try:
        y1, x1 = columnas[origen[0]], 8-int(origen[1])
        y2, x2 = columnas[destino[0]], 8-int(destino[1])
    except:
        print("Movimiento inválido: coordenadas fuera del tablero.")
        return False

    pieza = tablero[x1][y1]

    if pieza == ".":
        print("Movimiento inválido: no hay pieza en la casilla de origen.")
        return False

    # Verificar turno
    if turno == "blancas" and pieza.islower():
        print("No puedes mover piezas negras en el turno de blancas.")
        return False
    if turno == "negras" and pieza.isupper():
        print("No puedes mover piezas blancas en el turno de negras.")
        return False

    # Verificar si el movimiento es válido
    if not es_movimiento_valido(pieza, x1, y1, x2, y2):
        print("Movimiento inválido para la pieza:", pieza)
        return False

    # Ejecutar movimiento
    tablero[x2][y2] = pieza
    tablero[x1][y1] = "."

    # Cambiar turno
    turno = "negras" if turno == "blancas" else "blancas"
    return True


# ---- Juego en consola ----
mostrar_tablero()

while True:
    print("-------------------------------------")
    print(f"Turno de {turno}")
    print("-------------------------------------")
    origen = input("Origen (ej: e2): ")
    print("-------------------------------------")
    destino = input("Destino (ej: e4): ")
    print("-------------------------------------")

    if mover_pieza(origen, destino):
        mostrar_tablero()
