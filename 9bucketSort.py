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

def bucketSort(lista):
    if not lista:
        return []

    max_valor = max(lista)
    tamanho = len(lista)
    num_buckets = tamanho

    buckets = [[] for _ in range(num_buckets)]

    for numero in lista:
        index = int((numero / (max_valor + 1)) * num_buckets)
        buckets[index].append(numero)

    ordenada = []
    for bucket in buckets:
        ordenada.extend(insertionSort(bucket))

    return ordenada

lista = listaDesordenada()
ordenada = bucketSort(lista.copy())

print(f"Lista ordenada com Bucket Sort:\n{ordenada}")

'''
Bucket Sort
Como funciona:
Distribui os elementos em “baldes” (listas) com base em uma função de faixa.
Depois ordena cada balde individualmente (geralmente com Insertion Sort) e junta tudo.

Pontos fortes:

- Pode atingir quase O(n) se os dados forem uniformemente distribuídos

- Excelente desempenho em conjuntos de dados distribuídos de forma contínua

- Permite ordenações paralelas (cada bucket pode ser tratado separadamente)

Pontos fracos:

- Depende muito da distribuição dos dados — pode virar O(n²) se tudo cair num balde só

- Precisa de uma boa função de distribuição e número adequado de buckets

- Não funciona bem com dados muito concentrados ou altamente desbalanceados

Ideal para:
Listas de números reais ou decimais entre 0 e 1, ou quando os dados são uniformemente distribuídos. Muito usado em gráficos, jogos, simulações, processamento de imagens.
'''
