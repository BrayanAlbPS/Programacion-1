def dibujar_carta(valor, palo):
    print("+---------+")
    print(f"| {valor:<2}      |")
    print("|         |")
    print(f"|    {palo}    |")
    print("|         |")
    print(f"|      {valor:>2} |")
    print("+---------+")

def dibujar_carta_oculta():
    print("+---------+")
    print("|         |")
    print("|         |")
    print("|     ?   |")
    print("|         |")
    print("|         |")
    print("+---------+")
    
import random

valores = ["A", "2", "3", "4", "5", "6", "7",
           "8", "9", "10", "J", "Q", "K"]

palos = ["♥", "♦", "♣", "♠"]

baraja = []

for palo in palos:
    for valor in valores:
        baraja.append([valor, palo])
        
random.shuffle(baraja)

jugador = []
banca = []

for i in range(2):
    jugador.append(baraja.pop())
    banca.append(baraja.pop())
    
print("Cartas del jugador:")
for carta in jugador:
    print(carta[0], carta[1])

print("\nCartas de la banca:")
print(banca[0][0], banca[0][1])
print("Carta oculta")

print("\nCartas restantes:", len(baraja))

print("Cartas del jugador:")
dibujar_carta(jugador[0][0], jugador[0][1])
dibujar_carta(jugador[1][0], jugador[1][1])

print("\nCartas de la banca:")
dibujar_carta(banca[0][0], banca[0][1])
dibujar_carta_oculta()

def calcular_puntuacion(mano):
    puntos = 0
    ases = 0

    for carta in mano:
        valor = carta[0]

        if valor == "A":
            puntos += 11
            ases += 1

        elif valor in ["J", "Q", "K"]:
            puntos += 10

        else:
            puntos += int(valor)


    while puntos > 21 and ases > 0:
        puntos -= 10
        ases -= 1
    return puntos


def turno_jugador(baraja, mano):
    while True:
        puntuacion = calcular_puntuacion(mano)
        print(f"\nAhora tu puntuacion es de:{puntuacion}")
        
        if puntuacion > 21:
            print("Pasaste de 21, perdiste")
            return False
        if puntuacion == 21:
            print("Haz obtenido 21 puntos exactos")
            return False
            
        opcion = input("Pedir otra carta (s)///// plantarte (d)? ").strip().lower()
        if opcion == 's':
            carta_nueva = baraja.pop()
            mano.append(carta_nueva)
            print("\nRecibiste:")
            dibujar_carta(carta_nueva[0], carta_nueva[1])
        elif opcion == 'd':
            print("Te has plantado")
            return True
        else:
            print("Opcion no valida, elige otra carta con la tecla [s] y plantartse con [d]")

def turno_dealer(baraja, mano_dealer):
    print("\n--- TURNO DEL DEALER ---")
    print("Cartas del dealer:")
    for carta in mano_dealer:
        dibujar_carta(carta[0], carta[1])
        
    puntuacion_dealer = calcular_puntuacion(mano_dealer)
    print(f"Puntuación inicial del dealer: {puntuacion_dealer}")
    
    while puntuacion_dealer < 17:
        print("\nEl dealer tiene menos de 17, pide otra carta...")
        carta_nueva = baraja.pop()
        mano_dealer.append(carta_nueva)
        dibujar_carta(carta_nueva[0], carta_nueva[1])
        puntuacion_dealer = calcular_puntuacion(mano_dealer)
        print(f"Nueva puntuacion del dealer: {puntuacion_dealer}")
        
    print(f"\nEl dealer se planta con: {puntuacion_dealer}")
    return puntuacion_dealer

def es_blackjack(mano):
    return len(mano) == 2 and calcular_puntuacion(mano) == 21

def determinar_ganador(mano_jugador, mano_dealer):
    puntos_j = calcular_puntuacion(mano_jugador)
    puntos_d = calcular_puntuacion(mano_dealer)
    
    bj_j = es_blackjack(mano_jugador)
    bj_d = es_blackjack(mano_dealer)
    
    print("\n///////////////////////////////")
    print("      -Resultados-         ")
    print("///////////////////////////////a")
    print(f"Tus puntos: {puntos_j} | Puntos de la banca: {puntos_d}")
    
    if puntos_j > 21:
        print("Ha ganado el dealer, pasaste de 21")
        return

    if puntos_d > 21:
        print("Haz ganado tu, el dealer paso de 21")
        return

    if bj_j and bj_d:
        print("Push (empate) ambos tienen Blackjack.")
    elif bj_j:
        print("Haz ganado con un Blackjack!")
    elif bj_d:
        print("Ha ganado el dealer, obtuvo Blackjack")
    
    else:
        if puntos_j > puntos_d:
            print("Haz ganado por que tienes mas puntos que el dealer")
        elif puntos_d > puntos_j:
            print("Ha ganado el dealer por que tiene mas puntos que tu")
        else:
            if len(mano_jugador) >= 3 and len(mano_dealer) >= 3:
                print("Push (Empate) ambos consiguieron la misma puntuación con 3 o mas cartas")
            else:
                print("Empate (push) nadie ha ganado")

if __name__ == "__main__":
    jugador_sigue_vivo = turno_jugador(baraja, jugador)
    
    if jugador_sigue_vivo:
        turno_dealer(baraja, banca)
        determinar_ganador(jugador, banca)
    else:
        print("\nFin del juego. Perdiste en tu turno.")