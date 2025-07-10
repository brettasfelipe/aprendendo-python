"""
Você vai criar uma agenda telefônica onde vários nomes podem ter o mesmo número de telefone. O programa deve ler n entradas, onde cada uma contém um nome e um número separados por vírgula e espaço (", "). Depois, o programa deve reorganizar a agenda de forma que os números sejam as chaves e os nomes (em tuplas) os valores.

A saída deve mostrar os números em ordem crescente, e os nomes associados em ordem alfabética.
"""

n = int(input()) # Salva o número de reps
lista_tel = {} 

for _ in range(n): # Itera o número de vezes especificado
    nome, numero = input().split(", ")
    if numero not in lista_tel: # Caso o numero esteja no dicionário
        lista_tel[numero] = (nome,)
    else: # Caso não esteja, altera a tupla anterior criando uma nova com o nome que se repete
        lista_tel[numero] = lista_tel[numero] + (nome,)

lista_tel_ord = {}
for key, value in lista_tel.items(): # Coloca em ordem alfabética os nomes
    lista_tel_ord[key] = tuple(sorted(value))

for key, value in sorted(lista_tel_ord.items()): # Coloca em ordem crescente os números
    print(f"{key}: {value}")


