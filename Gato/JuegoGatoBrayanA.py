import numpy as np
import matplotlib.pyplot as plt
def mostrar_tablero_ventana(tablero, mensaje=""):
    fig, ax = plt.subplots(figsize=(5, 5))
    
    ax.plot([1, 1], [0, 3], color='gray', linewidth=3)
    ax.plot([2, 2], [0, 3], color='gray', linewidth=3)
    ax.plot([0, 3], [1, 1], color='gray', linewidth=3)
    ax.plot([0, 3], [2, 2], color='gray', linewidth=3)
    
    for fila in range(3):
        for col in range(3):
            simbolo = tablero[fila, col]

            x = col + 0.5
            y = 2.5 - fila
            
            if simbolo == "X":
                ax.text(x, y, "X", fontsize=45, ha='center', va='center', color='red', fontweight='bold')
            elif simbolo == "O":
                ax.text(x, y, "O", fontsize=45, ha='center', va='center', color='blue', fontweight='bold')
                
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_xticks([0.5, 1.5, 2.5])
    ax.set_xticklabels(["Col 1", "Col 2", "Col 3"], fontsize=11)
    ax.set_yticks([2.5, 1.5, 0.5])
    ax.set_yticklabels(["Fila 1", "Fila 2", "Fila 3"], fontsize=11)

    
    if mensaje:
        plt.title(mensaje, fontsize=14, fontweight='bold', pad=15)
    else:
        plt.title("Juego del Gato", fontsize=14, fontweight='bold', pad=15)
        
    plt.tight_layout()
    plt.show()
def mostrar_tablero(tablero):
    print("\n    1   2   3")
    for i in range(3):
        print(f"{i+1}   {tablero[i,0]} | {tablero[i,1]} | {tablero[i,2]}")
        if i < 2:
            print("   ---+---+---")
def verificar_ganador(tablero, jugador):

    for i in range(3):
        if np.all(tablero[i, :] == jugador) or np.all(tablero[:, i] == jugador):
            return True
            
    if np.all(np.diag(tablero) == jugador) or np.all(np.diag(np.fliplr(tablero)) == jugador):
        return True
        
    return False

def jugar_gato():

    tablero = np.full((3, 3), " ", dtype=str)
    jugador_actual = "X"
    turnos = 0
    
    print("--Bienvenido al juego del gatito (Tres en raya para 2 jugadores)")
    print("--Cada vez que se muestre la ventana del juego, presiona [q] para quitar la ventana")
    print("--Despues selecciona la fila y columna para hacer la jugada del turno, esto actualizara la ventana")
    mostrar_tablero_ventana(tablero, "Tablero Inicial - Turno: X")
    
    while True:
        mostrar_tablero(tablero)
        print(f"\nTurno de:'{jugador_actual}'")
        
        try:
            fila = int(input("Selecciona fila [1-3]:")) - 1
            col = int(input("Selecciona columna [1-3]:")) - 1
            
            if fila < 0 or fila > 2 or col < 0 or col > 2:
                print("Error: solo debes seleccionar coordenadas entre [1-3]")
                continue
                
            if tablero[fila, col] != " ":
                print("Error: ese espacio ya esta ocupado")
                continue
                
        except ValueError:
            print("Error: solo debes poner numeros enteros")
            continue
            
        tablero[fila, col] = jugador_actual
        turnos += 1
        
        if verificar_ganador(tablero, jugador_actual):
            mostrar_tablero(tablero)
            mensaje_final = f"El jugador {jugador_actual} ha ganado"
            print(f"\n{mensaje_final}")
            mostrar_tablero_ventana(tablero, mensaje_final)
            break
            
        if turnos == 9:
            mostrar_tablero(tablero)
            mensaje_final = "Empate, se llenaron todos los espacios, sin ganadores"
            print(f"\n{mensaje_final}")
            mostrar_tablero_ventana(tablero, mensaje_final)
            break
            
        jugador_actual = "O" if jugador_actual == "X" else "X"
        mostrar_tablero_ventana(tablero, f"Turno de:{jugador_actual}")

if __name__ == "__main__":
    jugar_gato()