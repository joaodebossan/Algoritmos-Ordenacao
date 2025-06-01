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

def mergeSort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = mergeSort(lista[:meio])
    direita = mergeSort(lista[meio:])

    return mergeS(esquerda, direita)

def mergeS(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

lista = listaDesordenada()
ordenada = mergeSort(lista)

print(f"Lista ordenada com Merge Sort:\n{ordenada}")

'''
Merge Sort
Como funciona:
Divide a lista em duas até ter só elementos únicos e depois mescla tudo em ordem.

Pontos fortes:

- Complexidade garantida: O(n log n) mesmo no pior caso

- Muito estável

- Excelente para listas grandes

- Usado quando é necessário manter a estabilidade da ordenação

Pontos fracos:

- Usa mais memória: cria muitas listas temporárias

- Mais lento que Quick Sort na média (mas mais seguro)

Ideal para:
Listas muito grandes ou quando a estabilidade da ordenação importa (ex: ordenar por nome sem bagunçar a ordem anterior).
'''
