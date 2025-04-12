import random
import time
import csv

TOP_DOWN = "TOP_DOWN"
BOTTOM_UP = "BOTTOM_UP"

def merge(lista, low, mid, high):
    for i in range(low, high + 1):
        aux[i] = lista[i]

    k = low
    j = mid + 1

    for i in range(low, high + 1):
        if k > mid:
            lista[i] = aux[j]
            j += 1
        elif j > high:
            lista[i] = aux[k]
            k += 1
        elif aux[j] < aux[k]:
            lista[i] = aux[j]
            j += 1
        else:
            lista[i] = aux[k]
            k += 1

def merge_sort_bottom_up(arr):
    n = len(arr)

    size = 1
    while size < n:
        for low in range(0, n - size, size * 2):
            mid = low + size - 1
            high = min(low + size * 2 - 1, n - 1)
            merge(arr, low, mid, high)
        size *= 2

def merge_sort_top_down(lista, low, hi):
    if hi <= low:
        return
    mid = low + (hi - low) // 2
    merge_sort_top_down(lista, low, mid)
    merge_sort_top_down(lista, mid + 1, hi)
    merge(lista, low, mid, hi)

def run_mergesort(nome_alg, lista, type):
    global aux
    aux = [0] * len(lista) 
    copia = lista.copy()
    start = time.time()
    if(type == BOTTOM_UP):
        merge_sort_bottom_up(lista)
    elif(type == TOP_DOWN):
        merge_sort_top_down(lista, 0, len(copia) - 1)
    end = time.time()
    tempo = (end - start) * 1000
    print(f"{nome_alg}: {tempo:.2f} ms")


def generate_random_array(n, seed=588622):
    random.seed(seed)
    return [random.randint(0, 10000) for _ in range(n)]

def salvar_em_txt(lista, nome):
    with open(f"{nome}.txt", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(lista)

tamanhos = [1000, 10000, 100000, 1000000]

for tam in tamanhos:
    print(f"\n--- Tamanho: {tam} elementos ---")
    lista = generate_random_array(tam)
    salvar_em_txt(lista, str(tam))

    aux = []* len(lista)

    run_mergesort("Mergesort - TOP DOWN", lista, TOP_DOWN)
    run_mergesort("Mergesort - BOTTOM UP", lista, BOTTOM_UP)