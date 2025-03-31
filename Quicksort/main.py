def quicksort_lomuto_first_key(lista, i, f):
    if(f > i):
        p = partition_lomuto_first_key(lista, i, f)
        quicksort_lomuto_first_key(lista, i, p - 1)
        quicksort_lomuto_first_key(lista, p+1, f)


def quickstort_lomuto_random_key(lista, i, f):
    if(f>i):
        p = partition_lomuto_first_key(lista, i, f)
        quicksort_lomuto_first_key(lista, i, p - 1)
        quicksort_lomuto_first_key(lista, p+1, f)   

def partition_lomuto_first_key(lista, left, right):
    chave = lista[left] # Pega primeiro valor como pivo
    storeIndex = left + 1
    for i in range(left + 1, right + 1):
        if(lista[i] < chave):
            lista[i], lista[storeIndex] = lista[storeIndex], lista[i]
            storeIndex += 1

    lista[left], lista[storeIndex - 1] = lista[storeIndex - 1], lista[left]
    return (storeIndex - 1)

def partition_lomuto_random_key(lista, left, right):
    index_random = random.randint(left, right)
    lista[left], lista[index_random] = lista[index_random], lista[left]
    chave = lista[index_random]
    storeIndex = left + 1
    for i in range(left + 1, right + 1):
        if(lista[i] < chave):
            lista[i], lista[storeIndex] = lista[storeIndex], lista[i]
            storeIndex += 1
    
    lista[left], lista[storeIndex - 1] = lista[storeIndex - 1], lista[left]
    return (storeIndex - 1)




lista = [10, 2, 5, 20, 14, 23, 8, 3, 5, 7]
lista2 = [10, 2, 5, 20, 14, 23, 8, 3, 5, 7]
quicksort_lomuto_first_key(lista, 0, len(lista) - 1)
quickstort_lomuto_random_key(lista2, 0, len(lista2) - 1)

print(lista)
print(lista2)