import random
import time

# Define simulados (constantes)
FIRST_VALUE = "FIRST_VALUE"
RANDOM_VALUE = "RANDOM_VALUE"
LOMUTO = "LOMUTO"
HOARE = "HOARE"

def quicksort_lomuto_first_key(lista, i, f):
    if f > i:
        p = partition_lomuto_first_key(lista, i, f)
        quicksort_lomuto_first_key(lista, i, p - 1)
        quicksort_lomuto_first_key(lista, p + 1, f)

def quicksort_lomuto_random_key(lista, i, f):
    if f > i:
        p = partition_lomuto_random_key(lista, i, f)
        quicksort_lomuto_random_key(lista, i, p - 1)
        quicksort_lomuto_random_key(lista, p + 1, f)

def quicksort_hoare_first_key(lista, i, f):
    if f > i:
        p = partition_hoare_first_key(lista, i, f)
        quicksort_hoare_first_key(lista, i, p)
        quicksort_hoare_first_key(lista, p + 1, f)

def quicksort_hoare_random_key(lista, i, f):
    if f > i:
        p = partition_hoare_random_key(lista, i, f)
        quicksort_hoare_random_key(lista, i, p)
        quicksort_hoare_random_key(lista, p + 1, f)

def partition_lomuto_first_key(lista, left, right):
    chave = lista[left]
    storeIndex = left + 1
    for i in range(left + 1, right + 1):
        if lista[i] < chave:
            lista[i], lista[storeIndex] = lista[storeIndex], lista[i]
            storeIndex += 1
    lista[left], lista[storeIndex - 1] = lista[storeIndex - 1], lista[left]
    return storeIndex - 1

def partition_lomuto_random_key(lista, left, right):
    index_random = random.randint(left, right)
    lista[left], lista[index_random] = lista[index_random], lista[left]
    chave = lista[left]
    storeIndex = left + 1
    for i in range(left + 1, right + 1):
        if lista[i] < chave:
            lista[i], lista[storeIndex] = lista[storeIndex], lista[i]
            storeIndex += 1
    lista[left], lista[storeIndex - 1] = lista[storeIndex - 1], lista[left]
    return storeIndex - 1

def partition_hoare_first_key(lista, left, right):
    chave = lista[left]
    i = left - 1
    j = right + 1
    while True:
        while True:
            i += 1
            if lista[i] >= chave:
                break
        while True:
            j -= 1
            if lista[j] <= chave:
                break
        if i >= j:
            return j
        lista[i], lista[j] = lista[j], lista[i]

def partition_hoare_random_key(lista, left, right):
    index_random = random.randint(left, right)
    lista[left], lista[index_random] = lista[index_random], lista[left]
    chave = lista[left]
    i = left - 1
    j = right + 1
    while True:
        while True:
            i += 1
            if lista[i] >= chave:
                break
        while True:
            j -= 1
            if lista[j] <= chave:
                break
        if i >= j:
            return j
        lista[i], lista[j] = lista[j], lista[i]

def quicksort(lista, pivot_type, partition_scheme):
    array = lista.copy()
    start_time = time.time()

    if partition_scheme == LOMUTO:
        if pivot_type == FIRST_VALUE:
            quicksort_lomuto_first_key(array, 0, len(array) - 1)
            nome = "Lomuto + First Value"
        elif pivot_type == RANDOM_VALUE:
            quicksort_lomuto_random_key(array, 0, len(array) - 1)
            nome = "Lomuto + Random Value"
    elif partition_scheme == HOARE:
        if pivot_type == FIRST_VALUE:
            quicksort_hoare_first_key(array, 0, len(array) - 1)
            nome = "Hoare + First Value"
        elif pivot_type == RANDOM_VALUE:
            quicksort_hoare_random_key(array, 0, len(array) - 1)
            nome = "Hoare + Random Value"
    else:
        raise ValueError("Partition scheme inválido")

    end_time = time.time()
    tempo = (end_time - start_time) * 1000
    print(f"{nome}: {tempo:.2f} ms")

def generate_random_array(n, seed=None):
    if seed is not None:
        random.seed(seed)
    return [random.randint(0, 10000) for _ in range(n)]

# Teste chamando com os "defines"
lista = generate_random_array(100000)

quicksort(lista, FIRST_VALUE, LOMUTO)
quicksort(lista, RANDOM_VALUE, LOMUTO)
quicksort(lista, FIRST_VALUE, HOARE)
quicksort(lista, RANDOM_VALUE, HOARE)
