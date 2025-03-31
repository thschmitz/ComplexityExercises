# Insertion Sort - Algoritmo de ordenação por inserção
def insertionSort(lista):
    """
    Implementação do Insertion Sort. Ordena a lista percorrendo os elementos um a um 
    e inserindo cada novo elemento na posição correta.

    Complexidade: O(n^2) no pior caso, O(n) no melhor caso (lista já ordenada).
    """
    for i in range(1, len(lista)):  # Percorre a lista a partir do segundo elemento
        key = lista[i]  # Elemento a ser inserido na posição correta
        j = i - 1  # Índice do elemento anterior
        # Move os elementos maiores que "key" uma posição à frente
        while j >= 0 and key < lista[j]:  
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key  # Insere o elemento na posição correta

    return lista  # Retorna a lista ordenada

lista = [2, 3, 4, 1, 2, 3, 10, 5, 7, 3, 7]

insertionSort(lista)

print(lista)