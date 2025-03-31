import random
import csv
import time

seq_potencia_2 = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576]
seq_3nplus1 = [1,4,13,40,121,364,1093,3280,9841,29524,88573,265720,797161,2391484]
seq_ciura = [1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711]

# Shell Sort - Algoritmo de ordenação com gaps
def shell_sort(arr, gaps):
    movimentacoes = 0
    gaps.reverse()

    n = len(arr)

    for gap in gaps:
        for start_index in range(gap):
            for i in range(start_index+gap, n, gap):
                temp = arr[i]
                j = i
                while j - gap >=start_index and arr[j - gap] > temp:
                    arr[j] = arr[j-gap]
                    j-=gap
                    movimentacoes += 1
                arr[j] = temp

    return arr, movimentacoes

def generate_random_array(n, seed=None):
  if seed is not None:
    random.seed(seed)
  random_array = [random.randint(0, 10000) for _ in range(n)]  # Generates numbers between 0 and 10000
  return random_array


def some_function():
    for _ in range(1000000):
        pass  # Example loop

# passe os parâmetros para gerar o vetor aleatório
seed = 588622 # id do portal do aluno
tamanho = 10 # tamanho do vetor

print("SHELL SORT")
print()

lista = [seq_potencia_2, seq_3nplus1, seq_ciura]
listaNomes = ["Potencia de 2", "3n+1", "Ciura"]
for i in range(3):
    array = generate_random_array(100000)
    print(f"Using sequence: {listaNomes[i]}")

    start_time = time.time()
    sorted_array_100, movimentacoes = shell_sort(array, lista[i])
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000 

    print(f"Execution time for shell_sort: {execution_time:.6f} ms")
    print("Numero de movimentacoes: ", movimentacoes)
    print()

    with open('array_1000.txt', 'w', newline='') as txtfile:
        writer = csv.writer(txtfile)
        writer.writerow(array)
#
#print()
#print("Potencias de 2")
#print()
#
#array100 = generate_random_array(100)
#start_time = time.time()
#
#sorted_array_100, movimentacoes = shell_sort(array100, seq_potencia_2)
#
#end_time = time.time()
#execution_time = (end_time - start_time) * 1000 
#
#print(f"Execution time for shell_sort seq_potencia_2: {execution_time:.6f} ms")
#print("Numero de movimentacoes: ", movimentacoes)
#
#print()
#print("3n+1")
#print()
#
## 3N + 1
#array100_2 = generate_random_array(100)
#start_time = time.time()
#
#sorted_array_100_2, movimentacoes = shell_sort(array100_2, seq_3nplus1)
#
#end_time = time.time()
#execution_time = (end_time - start_time) * 1000
#
#print(f"Execution time for shell_sort seq_3n+1: {execution_time:.6f} ms")
#print("Numero de movimentacoes: ", movimentacoes)
#
#print()
#print("Ciura")
#print()
#
## Ciura
#array100_3 = generate_random_array(100)
#
#start_time = time.time()
#
#sorted_array_100_3, movimentacoes = shell_sort(array100_3, seq_ciura)
#
#end_time = time.time()
#execution_time = (end_time - start_time) * 1000
#
#print(f"Execution time for shell_sort Ciura: {execution_time:.6f} ms")
#print("Numero de movimentacoes: ", movimentacoes)
#
#
## salve no formato CSV
#with open('array_100.csv', 'w', newline='') as csvfile:
#    writer = csv.writer(csvfile)
#    writer.writerow(array100)