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
