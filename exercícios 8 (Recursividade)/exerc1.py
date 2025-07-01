"""
Implemente uma função recursiva chamada imprimeTermos que receba um número inteiro n 
e imprima os termos da sequência n,n-2,n-4,...,0, isto é, os termos da sequência que começa pelo valor n
e termina em 0, decrescendo de 2 em 2 valores.
"""
def imprimeTermos(n):
    if n <= 0: # Caso base da recursividade, ao final ele deve printar 0
        print(0)
    else:
        print(n)
        return imprimeTermos(n-2) # Aproximação do caso base e chama a própria função

    

