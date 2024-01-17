# Estrategia 2: N Reinas usando Poda por Factibilidad.
# By: Jorge Ulises Zapata Arteaga.
# Analisis y Diseño de Algoritmos. 3CM2.

import time
import matplotlib.pyplot as plt

N = 12  # Tamaño del tablero
soluciones = 0  # Contador de soluciones encontradas
tiempos = []  # Arreglo para almacenar los tiempos de ejecución

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for i in range(N):
        for j in range(N):
            print(tablero[i][j], end=" ")
        print()
    print()

# Función para comprobar si se puede colocar una reina en la posición (fila, col)
def es_posicion_valida(tablero, fila, col):
    # Comprobar si hay una reina en la misma columna
    for i in range(fila):
        if tablero[i][col]:
            return False

    # Comprobar si hay una reina en la misma fila
    if 1 in tablero[fila]:
        return False

    # Comprobar si hay una reina en las diagonales
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j]:
            return False

    for i, j in zip(range(fila, -1, -1), range(col, N)):
        if tablero[i][j]:
            return False

    return True

# Función recursiva para encontrar las soluciones con poda por factibilidad
def encontrar_soluciones_con_poda(tablero, fila):
    global soluciones
    # Si se ha colocado una reina en cada fila, se ha encontrado una solución
    if fila == N:
        soluciones += 1
        tiempos.append(time.time() - encontrar_soluciones_con_poda.start_time)  # Almacenar el tiempo de ejecución
        return

    # Colocar una reina en cada columna de la fila actual y continuar con la siguiente fila
    for i in range(N):
        if es_posicion_valida(tablero, fila, i):
            tablero[fila][i] = 1
            encontrar_soluciones_con_poda(tablero, fila + 1)
            tablero[fila][i] = 0

if __name__ == "__main__":
    tablero = [[0] * N for _ in range(N)]

    # Medir el tiempo de ejecución global
    encontrar_soluciones_con_poda.start_time = time.time()
    encontrar_soluciones_con_poda(tablero, 0)

    if soluciones == 0:
        print("No se encontraron soluciones.")
    else:
        print("Se encontraron", soluciones, "soluciones.")
        
    # Imprimir el tiempo total de ejecución
    end_time = time.time()
    total_time = end_time - encontrar_soluciones_con_poda.start_time
    print("Tiempo total de ejecución:", total_time, "segundos")

    # Graficar el tiempo de ejecución
    plt.plot(range(1, soluciones + 1), tiempos, marker='o')
    plt.xlabel('Número de Soluciones Encontradas')
    plt.ylabel('Tiempo de Ejecución en segundos')
    plt.title('Tiempo de Ejecución del número de soluciones')
    plt.show()
