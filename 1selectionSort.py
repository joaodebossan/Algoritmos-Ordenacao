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

def selectionSort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

lista = listaDesordenada()
listaOrdenada = selectionSort(lista.copy())

print(f"Lista ordenada com Selection Sort:\n{listaOrdenada}")


'''
Selection Sort
Como  funciona: 
A cada iteração, encontra o menor elemento do restante da lista e coloca na posição certa.

Pontos fortes:

- Simples de implementar

- Número fixo de comparações (independente da ordem da lista)

- Boa escolha se trocas forem mais caras que comparações

Pontos fracos:

- Lento: sempre faz O(n²) comparações e trocas

- Não adaptativo: não melhora se a lista já estiver ordenada

- Pouco eficiente para listas grandes

Ideal para:
Aprender lógica de ordenação e ensinar algoritmos básicos. Pouco usado na prática.

'''