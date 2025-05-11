def bucketSort(lista):
    listaFinal = []
    aux = [[] for _ in range(len(lista))]

    for i in range(len(lista)):
        index = int(lista[i] * len(lista) / 1000)

        if not aux[index]:
            aux[index].append(lista[i])
        else:
            inserted = False
            for j in range(len(aux[index])):
                if lista[i] < aux[index][j]:
                    aux[index].insert(j, lista[i])
                    inserted = True
                    break
            if not inserted:
                aux[index].append(lista[i])
    for i in range(len(aux)):
        for j in range(len(aux[i])):
            listaFinal.append(aux[i][j])

    return listaFinal

lista = [10, 9, 456, 532, 3, 9, 2, 5]
listaFinal = bucketSort(lista)
print(listaFinal)