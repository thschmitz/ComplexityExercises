def bubbleSort(lista):
    troca = True
    while troca==True:
        troca = False
        for i in range(len(lista)-1):
            if(lista[i] > lista[i+1]):
                lista[i], lista[i+1] = lista[i+1], lista[i]
                troca = True


lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
bubbleSort(lista)
print(lista)