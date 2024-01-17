# Implementación inicial: N Reinas.
# By: Jorge Ulises Zapata Arteaga.
# Analisis y Diseño de Algoritmos. 3CM2.

import time
import matplotlib.pyplot as plt

N = 12  # Tamaño del tablero
soluciones = 0  # Contador de soluciones encontradas
tiempos_por_solucion = []  # Arreglo para almacenar los tiempos de cada solución

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

    # Comprobar si hay una reina en la diagonal principal superior
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j]:
            return False

    # Comprobar si hay una reina en la diagonal secundaria superior
    for i, j in zip(range(fila, -1, -1), range(col, N)):
        if tablero[i][j]:
            return False

    return True

# Función recursiva para encontrar las soluciones
def encontrar_soluciones(tablero, fila):
    global soluciones
    global tiempos_por_solucion
    # Si se ha colocado una reina en cada fila, se ha encontrado una solución
    if fila == N:
        soluciones += 1
        return

    # Colocar una reina en cada columna de la fila actual y continuar con la siguiente fila
    for i in range(N):
        if es_posicion_valida(tablero, fila, i):
            tablero[fila][i] = 1
            inicio = time.time()
            encontrar_soluciones(tablero, fila + 1)
            fin = time.time()
            tiempos_por_solucion.append(fin - inicio)
            tablero[fila][i] = 0

if __name__ == "__main__":
    tablero = [[0] * N for _ in range(N)]
    
    inicio_global = time.time()
    encontrar_soluciones(tablero, 0)
    fin_global = time.time()

    if soluciones == 0:
        print("No se encontraron soluciones.")
    else:
        print("Se encontraron", soluciones, "soluciones.")
    
    print("Tiempo de ejecución global:", fin_global - inicio_global, "segundos")

    plt.plot(range(1, soluciones + 1), tiempos_por_solucion[:soluciones], marker='o')
    plt.title('Tiempos de ejecución por solución')
    plt.xlabel('Número de solución')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.show()
