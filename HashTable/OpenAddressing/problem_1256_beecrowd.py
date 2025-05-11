## Link of beecrowd acception -> https://judge.beecrowd.com/en/runs/code/44956799

class Node:
    def __init__(self, elemento):
        self.elemento = elemento
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, id):
        return id % self.capacity
    
    def insert(self, elemento):
        index = self._hash(elemento)
        new_node = Node(elemento)

        if self.table[index] is None:
            self.table[index] = new_node
            self.size += 1
            return

        current = self.table[index]
        while current.next:
            current = current.next

        current.next = new_node
        self.size += 1


    def __str__(self):
        linhas = []
        for i in range(self.capacity):
            linha = f"{i}"
            current = self.table[i]
            while current:
                linha += f" -> {current.elemento}"
                current = current.next
            linha += " -> \\"
            linhas.append(linha)
        return "\n".join(linhas)


qtd = int(input())

listaTables = []

for i in range(qtd):
    info = input()
    table = HashTable(int(info.split(" ")[0]))
    elementos = input()
    listaElementos = elementos.split(" ")
    for i in range(int(info.split(" ")[1])):
        table.insert(int(listaElementos[i]))
    
    listaTables.append(table)

for i in range(len(listaTables)):
    print(listaTables[i].__str__())
    if(i != len(listaTables) - 1):
        print()