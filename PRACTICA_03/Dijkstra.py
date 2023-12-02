#Dijkstra en python Examen
#By: Jorge Ulises Zapata Arteaga
#Analisis y Diseño de Algoritmos. 3CM2.

import heapq
import time

class Grafo:
    def __init__(self): #Constructor.
        self.vertices = {}  # Diccionario para almacenar los vértices y sus aristas

    def agregar_vertice(self, vertice): #Funcion para agregar vértices
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, desde_vertice, hacia_vertice, peso): #Funcion para agregar vértices
        if desde_vertice in self.vertices and hacia_vertice in self.vertices:
            self.vertices[desde_vertice].append((hacia_vertice, peso))

def dijkstra(grafo, inicio): #Funcion principal
    distancias = {vertice: float('infinity') for vertice in grafo.vertices}
    distancias[inicio] = 0

    cola_prioridad = [(0, inicio)]

    while cola_prioridad: #Ciclo principal de dijkstra.
        distancia_actual, vertice_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[vertice_actual]: #Si la distancia  encontrada es mayor a la que teníamos almacenada en el diccionario distancias, se ignora ya que encontramos un camino más corto anteriormente.
            continue

        for adyacente, peso in grafo.vertices[vertice_actual]:
            distancia = distancia_actual + peso

            if distancia < distancias[adyacente]:
                distancias[adyacente] = distancia
                heapq.heappush(cola_prioridad, (distancia, adyacente))

    # Reemplaza "inf" por un mensaje de aviso.
    for vertice, distancia in distancias.items(): #Itera cada elemento del diccionario de distancias para ver que vértices no tiene camino y cambia el valor "inf" que da por default la consola, por el mensaje "infinito" 
        if distancia == float('inf'): #Aquí compara cuales distancias son infinitas.
            distancias[vertice] = "Infinito" #Se hace el cambio.

    return distancias

#Inician los Casos de prueba.
grafo = Grafo()
#Agregamos 8 vértices.
grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")
grafo.agregar_vertice("D")
grafo.agregar_vertice("E")
grafo.agregar_vertice("F")
grafo.agregar_vertice("G")
grafo.agregar_vertice("H")

#Agregamos 11 aristas ponderadas y dirigidas que conectan a los vértices
grafo.agregar_arista("A", "B", 3)
grafo.agregar_arista("A", "C", 1)
grafo.agregar_arista("B", "C", 2)
grafo.agregar_arista("C", "D", 5)
grafo.agregar_arista("B", "D", 4)
grafo.agregar_arista("D", "E", 5)
grafo.agregar_arista("C", "E", 6)
grafo.agregar_arista("E", "F", 8)
grafo.agregar_arista("E", "G", 7)
grafo.agregar_arista("F", "H", 10)
grafo.agregar_arista("G", "H", 9)

# Algoritmo de Dijkstra, 1 solo caso de prueba.
#vertice_inicio = "A"
#resultado = dijkstra(grafo, vertice_inicio)
#print(f"Caminos mínimos desde {vertice_inicio}: {resultado}")


inicio_tiempo1 = time.time()
resultado1 = dijkstra(grafo, "A")
fin_tiempo1 = time.time()
print(f"Tiempo de ejecución del Caso de prueba 1: {fin_tiempo1 - inicio_tiempo1} segundos")
print(f"Caminos mínimos desde A: {resultado1}\n")


inicio_tiempo2 = time.time()
resultado2 = dijkstra(grafo, "B")
fin_tiempo2 = time.time()
print(f"Tiempo de ejecución del Caso de prueba 2: {fin_tiempo2 - inicio_tiempo2} segundos")
print(f"Caminos mínimos desde B: {resultado2}\n")


inicio_tiempo3 = time.time()
resultado3 = dijkstra(grafo, "C")
fin_tiempo3 = time.time()
print(f"Tiempo de ejecución del Caso de prueba 3: {fin_tiempo3 - inicio_tiempo3} segundos")
print(f"Caminos mínimos desde C: {resultado3}\n")


inicio_tiempo4 = time.time()
resultado4 = dijkstra(grafo, "D")
fin_tiempo4 = time.time()
print(f"Tiempo de ejecución del Caso de prueba 4: {fin_tiempo4 - inicio_tiempo4} segundos")
print(f"Caminos mínimos desde D: {resultado4}\n")


inicio_tiempo5 = time.time()
resultado5 = dijkstra(grafo, "E")
fin_tiempo5 = time.time()
print(f"Tiempo de ejecución del Caso de prueba 5: {fin_tiempo5 - inicio_tiempo5} segundos")
print(f"Caminos mínimos desde E: {resultado5}\n")
