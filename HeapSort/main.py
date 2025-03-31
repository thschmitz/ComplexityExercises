def heapSort(lista):
    tam_variable = len(lista)
    build_heap(lista, tam_variable)
    for i in range(len(lista) - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        tam_variable -= 1
        heapify(lista, 0, tam_variable)

def build_heap(lista, tam):
    for i in range(tam//2-1, -1, -1):
        heapify(lista, i, tam)

def heapify(lista, i, tam):
    left = 2*i+1
    right = 2*i+2
    max = i

    if(left < tam and lista[left] > lista[i]):
        max = left


    if(right < tam and lista[right] > lista[max]):
        max = right
    
    if(max != i):
        lista[i], lista[max] = lista[max], lista[i]
        heapify(lista, max, tam)


lista = [32, 7, 3, 15, 13, 4, 21, 6, 2, 9, 1, 31, 45, 11, 5, 8]

print("HeapSort")
print()

heapSort(lista)

print(lista)
