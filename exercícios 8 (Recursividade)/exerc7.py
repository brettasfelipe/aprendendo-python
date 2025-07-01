"""
Implemente uma função chamada triangulo que recebe dois parâmetros x e size. A função deve imprimir um triângulo, composto por caracteres '+' (sem aspas simples), com base de tamanho size e deslocado de x espaços para a direita.
"""

def triangulo(x, size, atual=1): # Criação da função com um parametro de comparação
    d = x + size//2
    if atual == size: # Caso base
        print(d * " ","+".center(atual, "+"), sep="") 
    else:
        print(d * " ","+".center(atual, "+"), sep="")
        return triangulo(x-1, size, atual+2) # Chama a função novamente e se aproxima do caso base