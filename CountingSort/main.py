import random
import time
import csv
import tracemalloc  # ← novo

def radixsort(lista):
    aux = [0] * 10 
    finalList = [0] * len(lista)

    for element in lista:
        digito = element % 10
        aux[digito] += 1
    
    for i in range(1, len(aux)):
        aux[i] += aux[i-1]

    for i in range(len(lista)-1, -1, -1):
        digito = element % 10
        aux[digito] -= 1
        finalList[aux[digito]] = lista[i]

    return finalList

def run_radixsort(nome_alg, lista):

    tracemalloc.start()  # ← inicia rastreamento de memória

    start = time.time()
    radixsort(lista)
    end = time.time()

    current, peak = tracemalloc.get_traced_memory()  # ← mede memória

    tracemalloc.stop()  # ← finaliza rastreamento

    tempo = (end - start) * 1000
    print(f"{nome_alg}: {tempo:.2f} ms")
    print(f"Memória usada: {current / 1024:.2f} KB")
    print(f"Pico de memória: {peak / 1024:.2f} KB")
    
def monta_dict(lista):
    contagem = {}
    for item in lista:
        if item in contagem:
            contagem[item] += 1
        else:
            contagem[item] = 1
    return contagem

def countingSort(lista):
    contagem = monta_dict(lista)
    
    resultado = []
    for chave in sorted(contagem.keys()):
        resultado.extend([chave] * contagem[chave])
    
    return resultado

def run_countingsort(nome_alg, lista):
    tracemalloc.start()  # ← inicia rastreamento de memória

    start = time.time()
    countingSort(lista)
    end = time.time()

    current, peak = tracemalloc.get_traced_memory()  # ← mede memória

    tracemalloc.stop()  # ← finaliza rastreamento

    tempo = (end - start) * 1000
    print(f"{nome_alg}: {tempo:.2f} ms")
    print(f"Memória usada: {current / 1024:.2f} KB")
    print(f"Pico de memória: {peak / 1024:.2f} KB")

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

    run_countingsort("CountingSort", lista)
    run_radixsort("RadixSort", lista)