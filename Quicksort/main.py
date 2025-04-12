import random
import time
import csv
import tracemalloc  # ← novo

# Define constantes
FIRST_VALUE = "FIRST_VALUE"
RANDOM_VALUE = "RANDOM_VALUE"
LOMUTO = "LOMUTO"
HOARE = "HOARE"

# Define função de partição dinâmica
def partition(lista, left, right, pivot_type, partition_scheme):
    if pivot_type == RANDOM_VALUE:
        random_index = random.randint(left, right)
        lista[left], lista[random_index] = lista[random_index], lista[left]
    
    pivot = lista[left]

    if partition_scheme == LOMUTO:
        storeIndex = left + 1
        for i in range(left + 1, right + 1):
            if lista[i] < pivot:
                lista[i], lista[storeIndex] = lista[storeIndex], lista[i]
                storeIndex += 1
        lista[left], lista[storeIndex - 1] = lista[storeIndex - 1], lista[left]
        return storeIndex - 1
    
    elif partition_scheme == HOARE:
        i = left - 1
        j = right + 1
        while True:
            while True:
                i += 1
                if lista[i] >= pivot:
                    break
            while True:
                j -= 1
                if lista[j] <= pivot:
                    break
            if i >= j:
                return j
            lista[i], lista[j] = lista[j], lista[i]

    else:
        raise ValueError("Esquema de partição inválido")

# Função única de Quicksort
def quicksort(lista, i, f, pivot_type, partition_scheme):
    if f > i:
        p = partition(lista, i, f, pivot_type, partition_scheme)
        if partition_scheme == LOMUTO:
            quicksort(lista, i, p - 1, pivot_type, partition_scheme)
            quicksort(lista, p + 1, f, pivot_type, partition_scheme)
        elif partition_scheme == HOARE:
            quicksort(lista, i, p, pivot_type, partition_scheme)
            quicksort(lista, p + 1, f, pivot_type, partition_scheme)

def run_quicksort(nome_alg, lista, pivot_type, partition_scheme):
    copia = lista.copy()
    start = time.time()
    quicksort(copia, 0, len(copia) - 1, pivot_type, partition_scheme)
    end = time.time()

    current, peak = tracemalloc.get_traced_memory()  # ← mede memória

    tracemalloc.stop()  # ← finaliza rastreamento
    tempo = (end - start) * 1000
    print(f"{nome_alg}: {tempo:.2f} ms")
    print(f"Memória usada: {current / 1024:.2f} KB")
    print(f"Pico de memória: {peak / 1024:.2f} KB")

# Geração e salvamento de arrays
def generate_random_array(n, seed=588622):
    random.seed(seed)
    return [random.randint(0, 10000) for _ in range(n)]

def salvar_em_txt(lista, nome):
    with open(f"{nome}.txt", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(lista)

# Executa para vários tamanhos
tamanhos = [1000, 10000, 100000, 1000000]

for tam in tamanhos:
    print(f"\n--- Tamanho: {tam} elementos ---")
    lista = generate_random_array(tam)
    salvar_em_txt(lista, str(tam))

    run_quicksort("Lomuto + First Value", lista, FIRST_VALUE, LOMUTO)
    run_quicksort("Lomuto + Random Value", lista, RANDOM_VALUE, LOMUTO)
    run_quicksort("Hoare + First Value", lista, FIRST_VALUE, HOARE)
    run_quicksort("Hoare + Random Value", lista, RANDOM_VALUE, HOARE)
