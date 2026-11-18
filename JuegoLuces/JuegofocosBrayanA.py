import random
CANTIDAD = 10

ENCENDIDA = "○"

APAGADA = "●"
def crea_foco(cantidad, movimientos_mezcla=8):
    luces = [True] * cantidad
    while todas_encendidas(luces):
        for _ in range(movimientos_mezcla):
            seleccion(luces, random.randrange(cantidad))
    return luces

def seleccion(luces, posicion):
    for p in (posicion - 1, posicion, posicion + 1):
        if 0 <= p < len(luces):
            luces[p] = not luces[p]

def todas_encendidas(luces):
    return all(luces)

def mostrar_luces(luces):
    print()
    print("Numero de foco---" + "".join(f"{i + 1:<3}" for i in range(len(luces))))
    print("Foco-------------" + "".join((ENCENDIDA if luz else APAGADA) + "  " for luz in luces))
    print()
    print(f"{ENCENDIDA} Encendida   {APAGADA} Apagada")
    print()

def jugada(numero):
    while True:
        texto = input(f"Elige una posición (1-{numero}) o presiona [q-Q] para finalizar el juego").strip().lower()
        if texto == "q":
            return None
        if texto.isdigit() and 1 <= int(texto) <= numero:
            return int(texto) - 1
        print("No hay numero de foco con este numero [1-10]")

def jugar():
    luces = crea_foco(CANTIDAD)
    movimientos = 0
    print("Juego de los focos")
    print("Enciende todos los focos en el tablero")
    print("Al elegir un numero de foco, ese foco y sus cercanos cambiaran de apagado-prendido")

    while not todas_encendidas(luces):
        mostrar_luces(luces)
        posicion = jugada(CANTIDAD)
        if posicion is None:
            print("Juego terminado")
            return
        seleccion(luces, posicion)
        movimientos += 1

    mostrar_luces(luces)
    print(f"Haz ganado en {movimientos} turnos, felicitaciones")


if __name__ == "__main__":
    jugar()