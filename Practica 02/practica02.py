#Ordenamiento QuickSort.
#By: Jorge Ulises Zapata Arteaga.
#Análisis y Diseño de Algoritmos. 3CM2.

import random
import numpy as np
import matplotlib.pyplot as plt
import timeit

def quicksort(arreglo):
    if len(arreglo) <= 1:
        return arreglo
    else:
        pivote = sum(arreglo) / len(arreglo)
        menor = [x for x in arreglo if x < pivote]
        igual = [x for x in arreglo if x == pivote]
        mayor = [x for x in arreglo if x > pivote]
        return quicksort(menor) + igual + quicksort(mayor)

def arreglos(tamano):
    return [random.randint(1, 100) for i in range(tamano)]

num_arreglos = 100
longitud_Arreglos = [random.randint(1, 100) for i in range(num_arreglos)]
x_valores = []
y_valores = []

for i, tamano in enumerate(longitud_Arreglos, 1):
    arreglo = arreglos(tamano)
    print(f"Arreglo {i} original de tamaño {tamano}: {np.array(arreglo)}")
    time = timeit.timeit(lambda: quicksort(arreglo), number=1000)  
    x_valores.append(tamano)
    y_valores.append(time)
    print(f"Arreglo {i} ordenado de tamaño {tamano}: {np.array(quicksort(arreglo))}")
    print(f"Tardó {time} segundos en ordenarse.")

plt.plot(x_valores)
plt.xlabel('Longitud del arreglo')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución para los arreglos')
plt.show()
