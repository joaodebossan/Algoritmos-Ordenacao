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

def countingSort(lista):
    if not lista:
        return []

    maior_valor = max(lista)
    contagem = [0] * (maior_valor + 1)

    for numero in lista:
        contagem[numero] += 1

    ordenada = []
    for valor, frequencia in enumerate(contagem):
        ordenada.extend([valor] * frequencia)

    return ordenada

lista = listaDesordenada()
ordenada = countingSort(lista.copy())

print(f"Lista ordenada com Counting Sort:\n{ordenada}")

'''
Counting Sort
Como funciona:
Conta quantas vezes cada valor aparece na lista e reconstrói a lista ordenada com base nessa contagem.
Não compara elementos entre si.

Pontos fortes:

- Complexidade O(n + k), onde k é o maior valor da lista — super eficiente quando k não é muito maior que n

- Muito rápido para listas com valores inteiros pequenos e não negativos

- Algoritmo estável

Pontos fracos:

- Só funciona com números inteiros não negativos (precisa de adaptação para negativos)

- Pode desperdiçar muita memória se o intervalo de valores for muito grande

- Pouco flexível: não funciona com números decimais ou tipos complexos

Ideal para:
Listas inteiras pequenas, como dados de frequência, idades, notas de provas, etc. Ótimo em situações onde se sabe de antemão o intervalo de valores.
'''
