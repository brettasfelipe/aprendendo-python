"""
Implemente uma função recursiva chamada contagem_progressiva que recebe um número inteiro n e imprime os valores de 0 até n de forma crescente.
"""

# Cria a função com o parâmetro de parada e o inicial
def contagem_progressiva(n, inic=0):
    if inic == n: # Caso base da recursividade
        print(n)
    else:
        print(inic)
        return contagem_progressiva(n, inic+1) # Chama a função novamente se aproximando do caso base

