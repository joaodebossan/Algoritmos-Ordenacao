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

def quickSort(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[-1]
    menores = []
    iguais = []
    maiores = []

    for elemento in lista:
        if elemento < pivot:
            menores.append(elemento)
        elif elemento > pivot:
            maiores.append(elemento)
        else:
            iguais.append(elemento)

    return quickSort(menores) + iguais + quickSort(maiores)

lista = listaDesordenada()
ordenada = quickSort(lista)

print(f"Lista ordenada com Quick Sort:\n{ordenada}")

'''
Quick Sort
Como funciona:
Escolhe um pivô, divide em menores e maiores, e ordena recursivamente.

Pontos fortes:

- Muito rápido na prática

- Complexidade média: O(n log n)

- Usa pouca memória (em versões in-place)

- Funciona bem mesmo com listas grandes

Pontos fracos:

- Pior caso é O(n²) (quando o pivô é mal escolhido)

- Não é estável

- Recursivo: pode estourar pilha se mal implementado

Ideal para:
Ordenação geral de grandes volumes de dados, quando não precisa de estabilidade. É o queridinho de muitos sistemas por ser rápido e enxuto.
'''
