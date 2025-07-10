"""
Implemente uma função inversor_palavra(palavra) que, dada uma palavra (sem espaços), retorna a palavra invertida sem usar laços (for ou while) ou slicing ([::-1]).

Depois, faça um programa que leia uma string contendo várias palavras separadas por espaço, e imprima todas as palavras invertidas individualmente, separadas por espaço.
"""

# Criação da função recursiva
def inversor_palavra(palav, inic=-1): 
    if palav[inic] == palav[0]: # Caso base 
        return palav[0]
    else:
        return palav[inic] + inversor_palavra(palav, inic-1) # Se aproxima do caso base e chama a função
    
frase = input() 
t = 0 # Variável auxiliar pra dividir a string

for i in range(len(frase)):
    
    if frase[i] == " ": # Condição de parada 1 (Aparição de espaço)
        print(inversor_palavra(frase[t:i]), end=" ")
        t = i + 1

    elif i == len(frase)-1: # Condição de parada 2 (Fim da palavra)
        print(inversor_palavra(frase[t:i+1]))

    else: 
        pass
    
# Outra maneira:

for num, palavra in enumerate(frase.split()): # A função enumerate retorna um "índice" e a string
    print(inversor_palavra(palavra), end="\n" if num==len(frase.split())-1 else " ")

    
