import csv
import time

class Node:
    def __init__(self, id, nome, posicao):
        self.id = id
        self.nome = nome
        self.posicao = posicao
        self.next = None

class Est_Construcao:
    def __init__(self, tempo, taxa_ocupacao, tamanho_maximo, media_tamanho):
        self.tempo = tempo
        self.taxa_ocupacao = taxa_ocupacao
        self.tamanho_maximo = tamanho_maximo
        self.media_tamanho = media_tamanho

class Est_Consulta:
    def __init__(self, id, nome, numero_testes):
        self.id = id
        self.nome = nome
        self.numero_testes = numero_testes

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, id):
        return hash(id) % self.capacity
    
    def insert(self, id, nome, posicao):
        index = self._hash(id)

        if self.table[index] is None:
            self.table[index] = Node(id, nome)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.id == id:
                    current.nome = nome
                    current.posicao = posicao
                    return
                current = current.next
            
            new_node = Node(id, nome, posicao)

            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def sortedInsert(self, id, nome, posicao):
        index = self._hash(id)
        new_node = Node(id, nome, posicao)

        if self.table[index] is None:
            self.table[index] = new_node
            self.size += 1
            return

        current = self.table[index]
        previous = None

        while current and current.id < id:
            previous = current
            current = current.next

        if current and current.id == id:
            current.nome = nome
            current.posicao = posicao
            return

        new_node.next = current
        if previous is None:
            self.table[index] = new_node
        else:
            previous.next = new_node

        self.size += 1

    
    def binarySearch(self, id):
        index = self._hash(id)
        numero_testes = 0
        nodes = []
        current = self.table[index]
        while current:
            nodes.append((current.id, current.nome))
            current = current.next

        left, right = 0, len(nodes) - 1
        
        while left <= right:
            numero_testes += 1
            mid = (left + right) // 2
            if nodes[mid][0] == id:
                numero_testes += 1
                return nodes[mid], numero_testes
            elif nodes[mid][0] < id:
                numero_testes += 1
                left = mid + 1
            else:
                numero_testes += 1
                right = mid - 1

        return None, numero_testes



    def search(self, id):
        index = self._hash(id)
        numero_testes = 0
        current = self.table[index]
        while current:
            numero_testes += 1
            if current.id == id:
                return current, numero_testes

            current = current.next

    def remove(self, id):
        index = self._hash(id)

        previous = None
        current = self.table[index]

        while current:
            if current.id == id:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                
                self.size -= 1
                return
            previous = current
            current = current.next

    def __str__(self):
        elements = []
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                elements.append((current.id, current.nome))
                current = current.next
        return str(elements)
    
    def max_list(self):
        maximo = 0
        for i in range(self.capacity):
            count = 0
            current = self.table[i]
            while current:
                count += 1
                current = current.next
            if count > maximo:
                maximo = count
        return maximo


    def taxa_ocupacao_tabela(self):
        ocupacoes = self.capacity
        for i in range(self.capacity):
            if self.table[i] is None:
                ocupacoes -= 1
        return ocupacoes / self.capacity

    def media_tamanho_listas(self):
        soma_tamanho_listas = 0
        entradas_nao_vazias = 0
        for i in range(self.capacity):
            count = 0
            current = self.table[i]
            while current:
                count += 1
                current = current.next
            if count > 0:
                soma_tamanho_listas += count
                entradas_nao_vazias += 1
        if entradas_nao_vazias == 0:
            return 0
        return soma_tamanho_listas / entradas_nao_vazias


def estatisticas_construcao(tabela, caminho_csv, sorted):
    inicio = time.time()
    with open(caminho_csv, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            id = int(row["sofifa_id"])
            nome = row["name"]
            posicao = row["player_positions"]
            if(sorted == SORTED):
                tabela.sortedInsert(id, nome, posicao)
            else:
                tabela.insert(id, nome, posicao)
            

    fim = time.time()
    tempo = fim - inicio
    estatisticas = Est_Construcao(tempo, tabela.taxa_ocupacao_tabela(), tabela.max_list(), tabela.media_tamanho_listas())
    print(f"t{tabela.capacity}: {tempo:.6f} segundos")
    print(f"o{tabela.capacity}: {tabela.taxa_ocupacao_tabela()}")
    print(f"M{tabela.capacity}: {tabela.max_list()}")
    print(f"m{tabela.capacity}: {tabela.media_tamanho_listas()}")
    return estatisticas

def estatisticas_consultas(tabela, caminho_ids, sorted):
    import time

    inicio = time.time()

    with open(caminho_ids, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    lista_estatisticas_consulta = []

    for linha in linhas:
        id = int(linha.strip())
        if(sorted == SORTED):
            node, numero_testes = tabela.binarySearch(id)
        else:
            node, numero_testes = tabela.search(id)
        
        estatisticas = Est_Consulta(99999, "NAO_ENCONTRADO", numero_testes)

        if node:
            estatisticas.id = id
            estatisticas.nome = node[1]  

            print(f"c{tabela.capacity}: {id} - {estatisticas.nome} - {numero_testes}")
        else:
            print(f"c{tabela.capacity}: {estatisticas.id} - {estatisticas.nome} - {numero_testes}")
        
        lista_estatisticas_consulta.append(estatisticas)

    fim = time.time()
    tempo_final = fim - inicio
    print(f"\na({tabela.capacity}): {tempo_final:.6f} segundos")    

    return lista_estatisticas_consulta, tempo_final

def salvar_estatisticas_construcao(nome_arquivo, lista_estatisticas_construcao, capacidades):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(','.join([f'{int(est.tempo * 1000)}' for est in lista_estatisticas_construcao]) + '\n') 
        
        f.write(','.join([f'{est.taxa_ocupacao:.6f}' for est in lista_estatisticas_construcao]) + '\n')
        
        f.write(','.join([str(est.tamanho_maximo) for est in lista_estatisticas_construcao]) + '\n')
        
        f.write(','.join([f'{est.media_tamanho:.6f}' for est in lista_estatisticas_construcao]) + '\n')

def salvar_estatisticas_consultas(nome_arquivo, lista_estatisticas_consulta, lista_tempos_consulta, capacidades):
    # Mapeamento: id -> {nome, {capacidade: numero_testes}}
    mapa_resultados = {}

    # Preenche o mapa com os dados vindos das estatísticas individuais
    for i, est_lista in enumerate(lista_estatisticas_consulta):
        cap = capacidades[i]
        for est in est_lista:
            if est.id not in mapa_resultados:
                mapa_resultados[est.id] = {"nome": est.nome, "testes": {}}
            mapa_resultados[est.id]["testes"][cap] = est.numero_testes

    # Agora garante que todas as capacidades estejam presentes
    for id_jogador in mapa_resultados:
        for cap in capacidades:
            if cap not in mapa_resultados[id_jogador]["testes"]:
                mapa_resultados[id_jogador]["testes"][cap] = 0  # Força o preenchimento com 0

    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        # Primeira linha: tempos em milissegundos
        f.write(','.join([f'{int(t * 1000)}' for t in lista_tempos_consulta]) + '\n')

        # Linhas de saída: id,nome,testes_por_capacidade
        for id_jogador in sorted(mapa_resultados.keys()):
            nome = mapa_resultados[id_jogador]["nome"]
            testes = mapa_resultados[id_jogador]["testes"]
            linha = f'{id_jogador},{nome}'
            for cap in capacidades:
                linha += f',{testes[cap]}'
            f.write(linha + '\n')



tabela3793 = HashTable(3793)
tabela6637 = HashTable(6637)
tabela9473 = HashTable(9473)
tabela12323 = HashTable(12323)
tabela15149 = HashTable(15149)

caminho_players = "players.csv"
caminho_consultas = "consultas.csv"
SORTED = "SORTED"

lista_tabelas = [tabela3793, tabela6637, tabela9473, tabela12323, tabela15149]
lista_estatisticas_construcao = []
lista_estatisticas_consulta = []
lista_tempos_consulta = []

for i in range(len(lista_tabelas)):
    # Note que se eu colocar o SORTED para construir, preciso aplicar o SORTED para consultar... coerência
    estatistica_construcao = estatisticas_construcao(lista_tabelas[i], caminho_players, SORTED)
    lista_estatisticas_construcao.append(estatistica_construcao)
    estatistica_consulta, time_consultas = estatisticas_consultas(lista_tabelas[i], caminho_consultas, SORTED)
    lista_estatisticas_consulta.append(estatistica_consulta)
    lista_tempos_consulta.append(time_consultas)

capacidades = [3793, 6637, 9473, 12323, 15149]

salvar_estatisticas_construcao("estatisticas_construcao.txt", lista_estatisticas_construcao, capacidades)
salvar_estatisticas_consultas("estatisticas_consultas.txt", lista_estatisticas_consulta, lista_tempos_consulta, capacidades)
