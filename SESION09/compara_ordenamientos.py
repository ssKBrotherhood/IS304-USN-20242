import time
import random

# Algoritmo Bubble Sort
def bubble_sort(arr):
    lista = arr[:]
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Algoritmo Selection Sort
def selection_sort(arr):
    lista = arr[:]
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# Algoritmo Insertion Sort
def insertion_sort(arr):
    lista = arr[:]
    n = len(lista)
    for i in range(1, n):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista

# Algoritmo Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Función para medir el tiempo de ejecución de cada algoritmo
def medir_tiempos(lista):
    metodos = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort
    }
    
    tiempos = {}
    
    for nombre, metodo in metodos.items():
        inicio = time.time()
        metodo(lista)
        fin = time.time()
        tiempos[nombre] = fin - inicio
    
    # Ordenar los métodos por tiempo
    tiempos_ordenados = sorted(tiempos.items(), key=lambda x: x[1])
    return tiempos_ordenados

# Preguntar al usuario la cantidad de datos
cantidad_datos = int(input("Ingrese la cantidad de datos a generar: "))

# Generar una lista aleatoria con la cantidad indicada
lista_original = [random.randint(1, 10000) for _ in range(cantidad_datos)]

# Medir los tiempos de cada algoritmo
resultados = medir_tiempos(lista_original)

# Resultado final: tiempos ordenados
print("Tiempos de ejecución de los algoritmos:")
for metodo, tiempo in resultados:
    print(f"{metodo}: {tiempo:.6f} segundos")
