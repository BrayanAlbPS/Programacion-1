import matplotlib.pyplot as plt
import numpy as np
def carga_datos(nombre_archivo):
    """Lee el archivo línea por línea y retorna (dias, temperaturas, radiaciones)."""
    lista_dias = []
    lista_temperaturas = []
    lista_radiaciones = []

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            partes = linea.split(",")
            if len(partes) != 3:
                continue
            try:
                dia = int(partes[0])
                temp = float(partes[1])
                rad = float(partes[2])
            except ValueError:
                continue
            lista_dias.append(dia)
            lista_temperaturas.append(temp)
            lista_radiaciones.append(rad)

    dias = np.array(lista_dias, dtype=int)
    temperaturas = np.array(lista_temperaturas, dtype=float)
    radiaciones = np.array(lista_radiaciones, dtype=float)

    return (dias, temperaturas, radiaciones)

def analizar_clima(temperaturas, radiaciones):
    """Calcula e imprime estadísticas de temperatura y radiación."""
    temp_promedio = np.mean(temperaturas)
    temp_maxima = np.max(temperaturas)
    rad_promedio = np.mean(radiaciones)
    dia_maximo = int(np.argmax(temperaturas)) + 1

    print(f"Temperatura prom.:{temp_promedio:.2f} °C")
    print(f"Temperatura max. registrada:{temp_maxima:.2f} °C")
    print(f"Radiacion prom.:{rad_promedio:.2f} W/m²")
    print(f"La temperatura max. ha ocurrido en el dia {dia_maximo}")
def graficar_clima(dias, temperaturas, radiaciones):
    """Genera una figura con 2 subgraficas en una columna."""
    fig, (ax1, ax2) = plt.subplots(2, 1)

    ax1.plot(dias, temperaturas, color="red", marker="o")
    ax1.grid(True)
    ax1.set_title("Registro semanal de la temperatura:")
    ax1.set_xlabel("Día")
    ax1.set_ylabel("°C")
    ax2.bar(dias, radiaciones, color="orange")
    ax2.grid(True, alpha=0.3)
    ax2.set_title("Radiacon solar")
    ax2.set_xlabel("Dia")
    ax2.set_ylabel("w/m²")
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    dias, temperaturas, radiaciones = carga_datos("datos_de_clima_hermosillo_ultimos_50_dias.txt")
    analizar_clima(temperaturas, radiaciones)
    graficar_clima(dias, temperaturas, radiaciones)