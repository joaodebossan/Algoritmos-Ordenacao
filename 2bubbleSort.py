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

def bubbleSort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista = listaDesordenada()
ordenada = bubbleSort(lista.copy())

print(f"Lista ordenada com Bubble Sort:\n{ordenada}")

'''
Bubble Sort
Como funciona:
Percorre a lista várias vezes, trocando vizinhos fora de ordem. Os maiores “borbulham” para o final.

Pontos fortes:

- Muito fácil de entender e implementar

- Pode ser otimizado para parar se a lista já estiver ordenada (versão adaptativa)

Pontos fracos:

- Lento: O(n²) no pior caso

- Mesmo com otimizações, continua ineficiente em listas médias ou grandes

- Muitas trocas desnecessárias

Ideal para:
Ensino básico e quando a lista é muito pequena. Nunca é usado em produção.
'''