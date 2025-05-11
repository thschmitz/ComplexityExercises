import random
import time
import csv
import tracemalloc  # ← novo

LSD = "LSD"
MSD = "MSD"

def radix_sort_lsd(arr):
    if not arr:
        return arr

    # Encontra o maior número para saber o número de dígitos
    max_num = max(arr)
    exp = 1  # expoente para extrair o dígito (1 = unidades, 10 = dezenas, etc.)

    while max_num // exp > 0:
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        # Conta ocorrências dos dígitos atuais
        for i in range(n):
            index = (arr[i] // exp) % 10 # Esse % 10 pega o valor do digito atual. Ex: 802 na primeira chamado será ( 802 // 1) % 10 = 2, resto da divisao por 10
            count[index] += 1

        # Acumula as posições
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Constrói o output de forma estável
        for i in reversed(range(n)):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        # Copia para o array original
        for i in range(n):
            arr[i] = output[i]

        exp *= 10

R = 256  # radix (ASCII)
M = 15   # cutoff para insertion sort

def char_at(s, d):
    """Retorna o código do caractere na posição d de s, ou -1 se d >= len(s)."""
    if d < len(s):
        return ord(s[d])
    else:
        return -1

def char_at(s, d):
    """
    Retorna o código ASCII do caractere na posição 'd' da string 's'.
    Se 'd' estiver além do comprimento da string, retorna -1 (representa fim da string).
    Isso garante que strings curtas venham antes de strings longas com o mesmo prefixo.
    """
    return ord(s[d]) if d < len(s) else -1


def msd_sort(strings):
    """
    Função principal do algoritmo MSD Radix Sort.
    Cria o array auxiliar e inicia a ordenação recursiva a partir do primeiro caractere (posição 0).
    """
    aux = [None] * len(strings)  # Array auxiliar do mesmo tamanho da lista original
    _msd_sort(strings, 0, len(strings) - 1, 0, aux)  # Ordena do início ao fim


def _msd_sort(strings, start, end, char_pos, aux):
    """
    Ordena strings[start:end+1] com base no caractere na posição char_pos.
    Esta função é chamada recursivamente para cada posição de caractere.
    """
    if start >= end:
        return  # Subvetor com 0 ou 1 elemento já está ordenado

    R = 256  # Radix: número de caracteres possíveis (ASCII)
    count = [0] * (R + 2)  # Vetor de contagem com espaço para -1 até 255 (R + 2)

    # 1. Contar a frequência dos caracteres na posição char_pos
    for i in range(start, end + 1):
        c = char_at(strings[i], char_pos)  # Pega o caractere atual
        count[c + 2] += 1  # Desloca por +2 para acomodar -1

    # 2. Transformar contagens em índices de início (prefix sum)
    for r in range(R + 1):
        count[r + 1] += count[r]

    # 3. Redistribuir as strings no array auxiliar de acordo com os índices
    for i in range(start, end + 1):
        c = char_at(strings[i], char_pos)
        index = count[c + 1]  # posição correta no aux
        aux[index] = strings[i]
        count[c + 1] += 1  # avança o índice para o próximo com o mesmo caractere

    # 4. Copiar de volta do array auxiliar para o array original
    for i in range(start, end + 1):
        strings[i] = aux[i - start]  # i - start porque aux começa do zero

    # 5. Recursivamente ordenar cada subgrupo com o mesmo caractere atual
    for r in range(R):
        left = start + count[r]
        right = start + count[r + 1] - 1
        _msd_sort(strings, left, right, char_pos + 1, aux)  # Vai para o próximo caractere


def run_radixsort(nome_alg, tipo, lista):

    tracemalloc.start()  # ← inicia rastreamento de memória

    start = time.time()
    if(tipo == LSD):
        finalList = radix_sort_lsd(lista)
    elif(tipo == MSD):
        # CONVERSÃO PARA STRING: para ordenar corretamente com base em dígitos mais significativos
        str_lista = [str(x) for x in lista]
        msd_sort(str_lista)
        # CONVERSÃO DE VOLTA PARA INTEIRO (opcional)
        finalList = [int(x) for x in str_lista]    
    
    end = time.time()

    current, peak = tracemalloc.get_traced_memory()  # ← mede memória

    tracemalloc.stop()  # ← finaliza rastreamento

    tempo = (end - start) * 1000
    print(f"{nome_alg}: {tempo:.2f} ms")
    print(f"Memória usada: {current / 1024:.2f} KB")
    print(f"Pico de memória: {peak / 1024:.2f} KB")
    
    return finalList;

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
    finalListLSD = run_radixsort("RadixSort - LSD", LSD, lista)
    finalListMSD = run_radixsort("RadixSort - MSD", MSD, lista)