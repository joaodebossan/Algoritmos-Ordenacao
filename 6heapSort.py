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

def heap(lista, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heap(lista, n, maior)

def heapSort(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heap(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heap(lista, i, 0)

    return lista

lista = listaDesordenada()
ordenada = heapSort(lista.copy())

print(f"Lista ordenada com Heap Sort:\n{ordenada}")

'''
Heap Sort
Como funciona:
Transforma a lista em um heap máximo (uma árvore binária onde cada pai é maior que seus filhos).
Depois, vai extraindo o maior elemento (a raiz) e colocando no final da lista, reconstruindo o heap a cada passo.

Pontos fortes:

- Complexidade garantida: O(n log n) em todos os casos

- Não usa memória extra significativa (é feito in-place)

- Ótimo para situações onde o desempenho precisa ser estável e previsível

- Útil quando não pode haver surpresas no tempo de execução

Pontos fracos:

- Não é estável (pode alterar a ordem de elementos iguais)

- Mais complexo de implementar que os algoritmos básicos

- Pode ser mais lento que o Quick Sort na prática, apesar da mesma complexidade

Ideal para:
Sistemas que precisam de desempenho consistente e que não podem gastar memória com listas auxiliares. É usado em compiladores, engines de jogos, sistemas embarcados.
'''
