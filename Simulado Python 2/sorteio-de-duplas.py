"""
Você deve implementar um programa que sorteia duplas de estudantes a partir de uma lista de nomes. Os nomes devem ser organizados em tuplas de dois elementos, com os pares sorteados aleatoriamente.

Se a quantidade de nomes for ímpar, o último aluno deve ficar em uma tupla sozinho.
"""
from random import shuffle 

lista_alunos = []

while True: # Recebe entradas até a palavra "FIM" ser digitada
    nome = input()
    if nome == "FIM":
        break
    lista_alunos.append(nome)

shuffle(lista_alunos) # Bagunça a ordem da lista de alunos
lista_pares = []

if len(lista_alunos)%2 != 0: # Se o número de alunos for impar, o último fica em uma tupla sozinho
    lista_pares.append((lista_alunos.pop(-1),))
else: 
    pass

for i in range(0, len(lista_alunos)-1, 2): # Organiza as duplas entre os demais
    lista_pares.append((lista_alunos[i], lista_alunos[i+1]))

print(*lista_pares, sep="\n")