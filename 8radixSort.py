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

def countingSortdigito(lista, digito):
    n = len(lista)
    contagem = [0] * 10
    saida = [0] * n

    for numero in lista:
        indice = (numero // digito) % 10
        contagem[indice] += 1

    for i in range(1, 10):
        contagem[i] += contagem[i - 1]

    for i in range(n - 1, -1, -1):
        indice = (lista[i] // digito) % 10
        saida[contagem[indice] - 1] = lista[i]
        contagem[indice] -= 1

    return saida

def radixSort(lista):
    if not lista:
        return []

    maximo = max(lista)
    digito = 1

    while maximo // digito > 0:
        lista = countingSortdigito(lista, digito)
        digito *= 10

    return lista

lista = listaDesordenada()
ordenada = radixSort(lista.copy())

print(f"Lista ordenada com Radix Sort:\n{ordenada}")

'''
Radix Sort
Como funciona:
Ordena os números dígito por dígito, começando pelo dígito menos significativo (unidade).
Em cada passo, usa um algoritmo estável, geralmente o Counting Sort, para ordenar com base no dígito atual.

Pontos fortes:

- Complexidade O(d × (n + k)), onde d é o número de dígitos

- Extremamente rápido para listas de inteiros com poucos dígitos

- Estável

- Não faz comparações diretas entre os valores

Pontos fracos:

- Só funciona bem com números inteiros não negativos

- Pode consumir memória extra

- Não é ideal para números com muitos dígitos ou distribuições muito desiguais

Ideal para:
Grandes volumes de inteiros não negativos com dígitos limitados (ex: CPF, matrícula, código de produto). Também muito usado em hardware e sistemas de banco de dados.
'''
