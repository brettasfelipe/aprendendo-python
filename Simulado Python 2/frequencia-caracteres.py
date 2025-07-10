"""
Você deve criar um programa que conte a frequência de cada caractere alfabético (ignorando espaços, números e pontuação) em uma string. A contagem deve ser case-insensitive (ou seja, 'A' e 'a' contam como a mesma letra).

A saída deve mostrar os caracteres em ordem alfabética no formato caractere:quantidade.
"""

frase = input().lower() # Padroniza a entrada pra ser case insensitive
dict_freq = {} 

for i in frase:
    if i.isalpha(): # Checa se o i é uma letra
        
        if i in dict_freq: # Caso i já esteja no dicionário, incrementa em um o valor
            dict_freq[i] += 1
        
        else: # Caso não esteja, cria o par chave valor com valor 1
            dict_freq[i] = 1

    else: 
        pass

for key, value in sorted((dict_freq.items())): # Padroniza a saída como o pedido no enunciado
    print(f"{key}:{value}") 