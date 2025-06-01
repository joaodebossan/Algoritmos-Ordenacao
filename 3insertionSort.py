import random

def listaDesordenada():
    try:
        quantidade = int(input("Digite a quantidade de números que deseja na lista: "))
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser um número positivo maior que zero.")

        lista = list(range(quantidade))
        random.shuffle(lista)
        
        print("Lista gerada (desordenada):")
        print(lista)
        return lista

    except ValueError as e:
        print(f"Erro: {e}. Por favor, insira um número inteiro positivo.")
        return listaDesordenada()
    
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return listaDesordenada()

def insertionSort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

lista = listaDesordenada()
ordenada = insertionSort(lista.copy())

print(f"Lista ordenada com Insertion Sort:\n{ordenada}")

'''
Insertion Sort
Como funciona:
Pega cada elemento da lista e o insere na posição correta da parte que já está ordenada.

Pontos fortes:

- Excelente para listas quase ordenadas

- Poucas trocas: só movimenta o necessário

- Funciona bem com listas pequenas

- Simples e estável (mantém ordem dos iguais)

Pontos fracos:

- O(n²) no pior caso (lista invertida)

- Ainda lento para listas grandes

Ideal para:
Listas pequenas ou quase ordenadas. Muito usado como parte de algoritmos maiores (ex: no final de um Quick Sort).
'''
