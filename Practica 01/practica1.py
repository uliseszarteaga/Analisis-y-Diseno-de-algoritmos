#CÓDIGOS PRACTICA 1.
#By: Jorge Ulises Zapata Arteaga.
#Análisis y Diseño de Algoritmos 3CM2.

print('----------------------------------------------')
print('-                  MENU            ')
print('- 1. Ordenamiento Burbuja simple.')
print('- 2. Ordenamiento Burbuja optimizado/mejorado.')
print('- 3. Salir del programa.')
print('----------------------------------------------')
opc = int(input('Elija la opción del ordenamiento que desea utilizar: '))

if opc == 1:
    print('ESTAS USANDO ORDENAMIENTO BURBUJA SIMPLE.')
    num = int(input('Elija el tamaño de la lista de números a ordenar: '))
    lista = []
    for i in range(0, num):
        n = int(input('Número a ingresar:'))
        lista.append(n)

    print('Lista antes de ordenar: ')
    for i in lista:
        print(i, end=' ')
    # Algoritmo de ordenamiento de burbuja simple
    for j in range(0, num - 1):
        for i in range(0, num - 1 - j):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux

    print('\nLista después de ordenar utilizando burbuja simple: ')
    
    for i in lista:
        print(i, end=' ')
#Nota: En burbuja simple hace 64 comparaciones con 9 datos de entrada (O(n^2)).        
if opc == 2:
    print('ESTAS USANDO ORDENAMIENTO BURBUJA MEJORADO/OPTIMIZADO.')
    num = int(input('Elija el tamaño de la lista de números a ordenar: '))
    lista = []
    for i in range(0, num):
        n = int(input('Número a ingresar: '))
        lista.append(n)

    print('Lista antes de ordenar: ')
    for i in lista:
        print(i, end=' ')

    # Algoritmo de ordenamiento de burbuja optimizado
    n = len(lista)
    bandera_cambio = True 
    while bandera_cambio:
        bandera_cambio = False
        for i in range(0, n - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                bandera_cambio = True

    print('\nLista después de ordenar utilizando burbuja optimizado: ')
    for i in lista:
        print(i, end=' ')
#Nota: En burbuja optimizada hacen 56 comparaciones.

#Bandera_cambio sirve para verificar si hay cambios en un recorrido completo a la lista. Su funcion es 
#optimizar el algoritmo para detectar si la lista está completamente ordenada antes de completar las iteraciones.
if opc==3:
    print('Esto fue todo, nos vemos luego. ;)')
