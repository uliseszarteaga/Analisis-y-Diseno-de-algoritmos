# Estrategia 3: N Reinas usando Heurísticas.
# By: Jorge Ulises Zapata Arteaga.
# Analisis y Diseño de Algoritmos. 3CM2.

import time
import random
import matplotlib.pyplot as plt

N = 12  # Tamaño del tablero
soluciones = 0  # Contador de soluciones encontradas
tiempos = []  # Lista para almacenar los tiempos de ejecución
soluciones_encontradas = []  # Arreglo para almacenar el número de soluciones encontradas en cada iteración

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for i in range(N):
        for j in range(N):
            print(tablero[i][j], end=" ")
        print()
    print()

# Función para contar la cantidad de reinas que entran en conflicto en una posición.
def contar_conflictos(tablero, fila, col):
    conflictos = 0
    for i in range(N):
        if i != fila and (tablero[i][col] or abs(i - fila) == abs(col - tablero[i].index(1))):
            conflictos += 1
    return conflictos

# Función para encontrar la posición con menos conflictos para una reina en una fila específica
def encontrar_mejor_posicion(tablero, fila):
    conflictos_minimos = float('inf')
    posiciones_minimas = []

    for i in range(N):
        conflictos = contar_conflictos(tablero, fila, i)
        if conflictos < conflictos_minimos:
            conflictos_minimos = conflictos
            posiciones_minimas = [i]
        elif conflictos == conflictos_minimos:
            posiciones_minimas.append(i)

    return random.choice(posiciones_minimas)

# Función para inicializar el tablero aleatoriamente
def inicializar_tablero():
    return [[random.choice([0, 1]) for _ in range(N)] for _ in range(N)]

# Función principal para usar min_conflicts
def min_conflicts():
    global soluciones
    tablero = inicializar_tablero()
    
    for _ in range(N):
        for fila in range(N):
            mejor_posicion = encontrar_mejor_posicion(tablero, fila)
            tablero[fila] = [0] * N
            tablero[fila][mejor_posicion] = 1
    
    if es_tablero_valido(tablero):
        print("Solucion", soluciones + 1, ":")
        imprimir_tablero(tablero)
        soluciones += 1
        return tablero
    else:
        return None

# Función para verificar si un tablero es válido
def es_tablero_valido(tablero):
    for fila in range(N):
        for col in range(N):
            if tablero[fila][col] == 1 and contar_conflictos(tablero, fila, col) > 0:
                return False
    return True

if __name__ == "__main__":
    inicio = time.time() #Medimos el tiempo de ejecución

    while soluciones < 100:  
        tablero = min_conflicts()
        tiempos.append(time.time() - inicio)
        soluciones_encontradas.append(soluciones)

    fin = time.time()

    if soluciones == 0:
        print("No se encontraron soluciones.")
    else:
        print("Se encontraron", soluciones, "soluciones.")
    print("Tiempo total de ejecución:", fin - inicio, "segundos")

    plt.plot(tiempos, soluciones_encontradas, marker='o')
    plt.title('Tiempo de soluciones encontradas')
    plt.xlabel('Tiempo (segundos)')
    plt.ylabel('Número de soluciones encontradas')
    plt.show()
