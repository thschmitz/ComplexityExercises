def heapSort(lista, contador):
    tam_variable = len(lista)
    build_heap(lista, tam_variable, contador)
    print(lista)
    for i in range(len(lista) - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        contador += 1
        print(lista)
        tam_variable -= 1
        heapify(lista, 0, tam_variable, contador)
        print(lista)

def build_heap(lista, tam, contador):
    for i in range(tam//2-1, -1, -1):
        heapify(lista, i, tam, contador)

def heapify(lista, i, tam, contador):
    left = 2*i+1
    right = 2*i+2
    max = i

    if(left < tam and lista[left] > lista[i]):
        max = left


    if(right < tam and lista[right] > lista[max]):
        max = right
    
    if(max != i):
        lista[i], lista[max] = lista[max], lista[i]
        contador += 1
        heapify(lista, max, tam, contador)

contador = 0
lista = [10, 5, 4, 3, 2, 9, 11, 14, 13]

print("HeapSort")
print()

heapSort(lista, contador)

print(lista)
print(contador)
