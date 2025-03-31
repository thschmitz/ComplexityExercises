# Selection Sort - Algoritmo de ordenação por seleção
def selectionSort(lista):
    """
    Implementação do Selection Sort. Ordena a lista encontrando sempre o menor 
    elemento e colocando-o na posição correta.

    Complexidade: O(n^2) no pior e melhor caso.
    """
    for i in range(0, len(lista)):  # Percorre a lista inteira
        key = lista[i]  # Armazena o valor atual
        min_index = i  # Define o índice do menor elemento na iteração atual
        # Percorre a sublista para encontrar o menor valor
        for j in range(i, len(lista)):
            if lista[j] < lista[min_index]:  # Atualiza o índice do menor valor
                min_index = j

        lista[i] = lista[min_index]  # Coloca o menor valor encontrado na posição correta
        lista[min_index] = key  # Troca os elementos

    return lista  # Retorna a lista ordenada


lista = [1, 2, 4, 5, 2, 3, 10, 2, 13, 29, 4, 7]

selectionSort(lista)

print(lista)